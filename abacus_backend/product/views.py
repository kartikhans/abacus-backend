from django.db.models import Q
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from product.models import Product
from product.serializers import AddProductSerailizer, UpdateProductSerailizer, ViewProductSerializer
from product.utils import manage_product
# Create your views here.


class addProduct(APIView):
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = AddProductSerailizer(data=data)
        result = {}

        if serializer.is_valid():
            data = serializer.validated_data
            result = manage_product.add_product(data)
        else:
            result['result'] = serializer.errors
            result['product_pid'] = None
            result['status'] = status.HTTP_404_NOT_FOUND

        return Response(result, status=result.get('status'))

class updateProduct(APIView):
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = UpdateProductSerailizer(data=data)
        result = {}

        if serializer.is_valid():
            data = serializer.validated_data
            result = manage_product.update_product(data)
        else:
            result['result'] = serializer.errors
            result['product_pid'] = None
            result['status'] = status.HTTP_404_NOT_FOUND

        return Response(result, status=result.get('status'))

class viewProduct(APIView):
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = ViewProductSerializer(data=data)
        result = {}

        if serializer.is_valid():
            data = serializer.validated_data
            result = manage_product.view_product(data)
        else:
            result['result'] = serializer.errors
            result['product_pid'] = None
            result['status'] = status.HTTP_404_NOT_FOUND

        return Response(result, status=result.get('status'))

class viewAllProduct(APIView):
    def post(self, request, format=None):
        result = manage_product.view_all_product()
        return Response(result, status=result.get('status'))