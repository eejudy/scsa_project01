from django.conf import settings
from django.db import models

# score로 변경
class User(models.Model):
    username = models.CharField(max_length=15, unique=True)
    score = models.IntegerField()
