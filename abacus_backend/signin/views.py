from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .utils import user_signin
from .serializers import UserSignInRequestSerializer


# Create your views here.
class UserSignIn(APIView):
    def post(self, request, format=None):
        data = JSONParser.parse(request)
        serializer = UserSignInRequestSerializer(data=data)
        result = {}
        if serializer.is_valid():
            result = user_signin.userSignIn(data)
        else:
            result['result'] = serializer.errors
            result['status'] = status.HTTP_404_NOT_FOUND

        return Response(result, status=result.get('status'))
