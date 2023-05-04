from django.db import models

class User(models.Model):
    username = models.CharField(max_length=15)
    age = models.IntegerField()
    city = models.CharField(max_length=15)
    