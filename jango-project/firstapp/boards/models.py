from django.conf import settings
from django.db import models
from django.utils import timezone

# score로 변경
class User(models.Model):
    username = models.CharField(max_length=6, unique=True)
    score = models.IntegerField()
    # city = models.CharField(max_length=15)

class Result(models.Model):
    num = models.IntegerField()
