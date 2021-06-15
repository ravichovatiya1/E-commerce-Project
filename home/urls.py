from django.urls import path,include
from home import views

app_name ='home'


urlpatterns = [
    path('', views.homepage,name = 'home'),
    path('product-detail/<int:pk>/',views.product_detail,name= 'product_detail'),
    path('shop-grid-left/<int:pk>/', views.shop_grid_left,name = 'shop_grid_left'),
    path('shop-grid-left/', views.all_shop_grid_left,name = 'all_shop_grid_left'),
    path('shop-grid-left-sub-category/<int:pk>/', views.shop_grid_left_sub_category,name = 'shop_grid_left_sub_category'),
    path('shop-grid-left-category/<int:pk>/', views.shop_grid_left_category,name = 'shop_grid_left_category'),

]
