from rest_framework import serializers
from product.models import Product


class AddProductSerailizer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=True)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']


class UpdateProductSerailizer(serializers.ModelSerializer):
    uid = serializers.UUIDField(required=True)
    name = serializers.CharField(max_length=200, required=True)

    class Meta:
        model = Product
        fields = ['uid', 'name', 'description', 'price', 'category', 'is_deleted']


class ViewProductSerializer(serializers.Serializer):
    uid = serializers.UUIDField(required=True)
