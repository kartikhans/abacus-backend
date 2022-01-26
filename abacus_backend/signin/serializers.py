from rest_framework import serializers
from abacus_backend.signup.models import User

class UserSignInRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "phone"]