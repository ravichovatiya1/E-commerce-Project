from django.urls import path,include
from cart import views


app_name ='cart'

urlpatterns = [
    path('',views.cart,name = 'cart'),
    path('add/cart/<int:pk>/',views.addCart,name='addCart'),
    path('update/cart/<int:pk>/',views.updateCart,name='updateCart'),
    path('remove-form-wishlist-to-cart/<int:pk>/',views.wish_to_cart,name='wish_to_cart'),
    path('remove/cart/<int:pk>/',views.removeCart,name = 'removeCart'),
    path('remove-all-cart/',views.removeAllCart,name = 'removeAllCart'),



]