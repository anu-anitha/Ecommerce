from django.shortcuts import render,redirect

# Create your views here.
from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import *

# Create your views here.
# serialized view using viewsets

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all().order_by('name')
#     serializer_class = CategorySerializer

def products(request):
	data=Product.objects.all()
	total_no_cart = OrderItem.objects.all().count()
	context = {'data':data, 'total_no_cart':total_no_cart}
	return render(request,'product.html',context)

def addcart(request,id):
	added_cart_product = Product.objects.get(pk = id)
	cart_products = OrderItem.objects.get_or_create(item = added_cart_product)
	return redirect('/')


def cartitems(request):
	cartitems = OrderItem.objects.all()
	context = {'cartitems':cartitems}
	return render(request,'cart.html',context)

def order_delete(request,id):
	Product.objects.get(pk=id).delete()
	return redirect('/')


# def add_to_cart(request):

