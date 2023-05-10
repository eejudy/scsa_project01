from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer, ResultSerializer
from .models import User, Result
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    queryset = User.objects.order_by('-score', '-id')[:10]
    serializer_class = UserSerializer
    # max_score = User.objects.last()

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    # max_score = User.objects.last()

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
    num = request.data.get("num")
    d = {'num':num}
    return Response(d)

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
        data = {'minn':minn.score}
        return Response(data)
    return Response(minn)

def index(request):
    return render(request, 'index.html') 

