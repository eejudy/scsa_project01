from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    queryset = User.objects.order_by('-score')[:10]
    serializer_class = UserSerializer
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