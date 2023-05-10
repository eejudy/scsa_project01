from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register('result', views.ResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("rank/", views.ranking),
    path('result_test/', views.result_test),
    path('check_duplicate/', views.check_duplicate),
    path('min_score/', views.min_score),
]