from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("rank/", views.ranking),
]