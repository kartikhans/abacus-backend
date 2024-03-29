from django.db.models import Q
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserSignUpRequestSerializer, UserSignInRequestSerializer, ChangePasswordSerializer, \
    UserProfileSerializer, UpdateUserSerializer
from .utils import user_signin, user_profile


# Create your views here.

class UserSignUp(APIView):
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = UserSignUpRequestSerializer(data=data)
        result = {}
        if serializer.is_valid():
            name = data.get('name')
            phone = data.get('phone')
            email = data.get('email')
            password = data.get('password')
            address = data.get('address')
            user_exists = User.objects.filter(Q(email=email) | Q(phone=phone)).exists()
            if not user_exists:
                user_object = User(name=name, phone=phone, email=email, password=password, address=address,
                                   is_deleted=False)
                user_object.save()
                result['result'] = "SUCCESS"
                result['status'] = status.HTTP_200_OK
            else:
                result['result'] = "Failed_due_to_similar_email_or_phone_exists"
                result['status'] = status.HTTP_404_NOT_FOUND
        else:
            result = {'result': serializer.errors, 'status': status.HTTP_404_NOT_FOUND}

        return Response(result, status=result.get('status'))


class UserSignIn(APIView):
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = UserSignInRequestSerializer(data=data)
        result = {}
        if serializer.is_valid():
            result = user_signin.userSignIn(data)
        else:
            result['result'] = serializer.errors
            result['status'] = status.HTTP_404_NOT_FOUND

        return Response(result, status=result.get('status'))


class change_password(APIView):
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = ChangePasswordSerializer(data=data)
        if serializer.is_valid():
            user_uid = data.get('uid')
            previous_password = data.get('password')
            new_password = data.get('new_password')
            result = user_profile.change_user_password(user_uid=user_uid, previous_password=previous_password,
                                                       new_password=new_password)
        else:
            result = {'result': serializer.errors, 'status': status.HTTP_404_NOT_FOUND}
        return Response(result, status=result.get('status'))


class show_user_profile(APIView):
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            result = user_profile.userProfile(data)
        else:
            result = {'result': serializer.errors, 'status': status.HTTP_404_NOT_FOUND}
        return Response(result, status=result.get('status'))


class update_user(APIView):
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = UpdateUserSerializer(data=data)
        if serializer.is_valid():
            user_uid = data.get('uid')
            name = data.get('name')
            phone = data.get('phone')
            address = data.get('address')
            result = user_profile.update_user_profile(user_uid=user_uid, name=name, phone=phone, address=address)
        else:
            result = {'result': serializer.errors, 'status': status.HTTP_404_NOT_FOUND}
        return Response(result, status=result.get('status'))
