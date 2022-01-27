from rest_framework import serializers
from .models import User


class UserSignUpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'phone', 'address']


class UserSignInRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone', 'password']


class ChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(max_length=20, required=True, allow_null=False)
    uid = serializers.UUIDField(required=True)

    class Meta:
        model = User
        fields = ["uid", "password", "new_password"]


class UpdateUserSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(required=True)

    class Meta:
        model = User
        fields = ["uid", "name", "phone", "address"]


class UserProfileSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(required=True)

    class Meta:
        model = User
        fields = ["uid"]
