from . import views 
from django.urls import path


urlpatterns=[
	path('',views.products,name='products'),
	path('addcart/<str:id>/',views.addcart,name='addcart'),
	path('del/<str:id>/',views.order_delete,name='del'),
	path('cartitems',views.cartitems, name = 'cartitems'),

]

