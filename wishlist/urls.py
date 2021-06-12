from django.urls import path,include
from wishlist import views


app_name ='wishlist'

urlpatterns = [
        path('',views.wishlist,name='wishlist'),
        path('add/wishlist/<int:pk>/',views.addWish,name='addWish'),
        path('remove/wishlist/<int:pk>/',views.removeWish,name = 'removeWish'),
        path('remove-all-wish/',views.removeAllWish,name = 'removeAllWish'),


]
