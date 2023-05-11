from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer, ResultSerializer
from .models import User, Result
from rest_framework.decorators import api_view
from rest_framework.response import Response

# ML 사용 위한 import
import random
import numpy as np
import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader
from torch.autograd import Variable
from torchvision import datasets, transforms

from .AImodel import statistical
from .utils import get_hyp, on_device, make_data, seq_data, train_model

class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    queryset = User.objects.order_by('-score', '-id')[:10]
    serializer_class = UserSerializer
    # max_score = User.objects.last()

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    # max_score = User.objects.last()

@api_view(['POST','GET'])
def ranking(request):
    cnt = 0
    ranks = User.objects.order_by('id')
    curr_user = ranks.last()
    for n in User.objects.order_by('-score', '-id'):
        cnt += 1
        if n.username == curr_user.username:
            data = {'cnt':cnt, 'username': curr_user.username}
    return Response(data)

def index(request):
    return render(request, 'index.html') 

@api_view(['POST','GET'])
def check_duplicate(request):
    alreadyIN = User.objects.all()
    currIN = request.data.get('currIN')

    for n in alreadyIN:
        if n.username == currIN:
            data = {'check':False}
            return Response(data)

    data = {'check':True}
    return Response(data)

@api_view(['POST','GET'])
def min_score(request):
    userdata = User.objects.order_by('id')
    usercnt = userdata.last()
    minn = 0
    if len(userdata)>=10:
        minn_temp = User.objects.order_by('-score')
        minn = minn_temp[9]
        return Response(minn.score)
    return Response(minn)


device = on_device()
seed, data_dim, seq_length, hidden_dim, output_dim, learning_rate, epochs, batch_size, probability = get_hyp()

a = make_data(data_dim=data_dim, SEED=seed)
b = seq_data(a, window=seq_length, data_dim=data_dim, batch_size=50)
c = statistical(input_dim=data_dim, hidden_dim=hidden_dim, seq_len=seq_length, output_dim=output_dim, layers=1, p=probability)

@api_view(['POST','GET'])
def predict(request):
    global a, b, c
    start = request.data.get('start')
    num = request.data.get('num')

    if start:
        c, predict = train_model(c,b,epochs=epochs,lr=learning_rate,device=device)
        return Response(predict)

    else:
        a = make_data(data=a, data_dim=data_dim, SEED=seed, new=num)
        b = seq_data(a, window=seq_length, data_dim=data_dim, batch_size=50)
        c, predict = train_model(c,b,epochs=epochs,lr=learning_rate,device=device)
        return Response(predict)