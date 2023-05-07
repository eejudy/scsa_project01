from django.contrib import admin
from django.urls import path, include
from boards import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('', include('boards.urls')),

]

