from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('-score')[:10]
    serializer_class = UserSerializer

def index(request):
    return render(request, 'index.html')    