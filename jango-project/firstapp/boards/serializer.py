from rest_framework import serializers
from .models import User, Result

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'score')

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ("__all__")
