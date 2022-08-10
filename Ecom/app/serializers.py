from rest_framework import serializers

from django.contrib.auth.models import AbstractUser
from .models import *

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')
# after creating category moved to products to relate db





class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # to serialize image for emtire url(max_length important)
    image = serializers.ImageField(max_length=None, allow_empty_file=False, required=False)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category')




class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')