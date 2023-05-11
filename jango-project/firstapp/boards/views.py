from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer, ResultSerializer
from .models import User, Result
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

# ML 사용 위한 import
import random
import numpy as np
import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader
from torch.autograd import Variable
from torchvision import datasets, transforms

from .AImodel import statistical
from .utils import get_hyp, get_device, make_data, seq_data, train_model


class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    queryset = User.objects.order_by('-score', '-id')[:10]
    serializer_class = UserSerializer

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

@api_view(['POST','GET'])
def check_duplicate(request):
    alreadyIN = User.objects.all()
    currIN = request.data.get('currIN')

    for n in alreadyIN:
        if n.username == currIN:
            data = {'exp':'already exist'}
            return Response(data)

    data = {'exp':'not exist'}
    return Response(data)

def index(request):
    return render(request, 'index.html')   
    

@api_view(['POST','GET'])
def ranking(request):
    cnt = 0
    ranks = User.objects.order_by('id')
    curr_user = ranks.last()
    for n in User.objects.order_by('-score'):
        cnt += 1
        if n.username == curr_user.username:
            data = {'cnt':cnt, 'username': curr_user.username}
    return Response(data)


@api_view(['POST','GET'])
def result_test(request):
    # num = request.POST.get("num") # 실행x
    num = request.data.get("num")
    d = {'num':num}
    return Response(d)


@api_view(['POST','GET'])
def min_score(request):
    userdata = User.objects.order_by('id')
    usercnt = userdata.last()
    minn = 0
    if usercnt.id>=10:
        minn_temp = User.objects.order_by('-score')
        minn = minn_temp[10]
        data = {'minn':minn.score}
        return Response(data)
    return Response(minn)

def predictfrm(request):
    return render(request,"boards/predict_form.html")
    

# 예측결과를 제공하는 함수
a = make_data()
b, c = seq_data(a), statistical()
@api_view(['POST','GET'])  # 안되면 여기서 data로 변경
def predict(request):
    global a, b, c
    start = request.data.get('start')
    num = request.data.get('num')

    if start:
        c, predict = train_model(c,b)
        return Response(predict)

    #     a = make_data()
    #     b = statistical()

    else:
        a = make_data(data=a, new=num)
        b = seq_data(a)
        c, predict = train_model(c,b)
        return Response(predict)

    # result = predict_score(num, statistical)



