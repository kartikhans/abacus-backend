from rest_framework import serializers
from .models import User

class UserSignUpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'phone', 'address']
