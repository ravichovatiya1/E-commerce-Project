from django.urls import path,include
from home import views

app_name ='home'


urlpatterns = [
    path('', views.homepage,name = 'home'),
    # path('basepage/',views.basepage,name='basepage'),
    path('home-1/', views.homepage1,name = 'home1'),
    path('home-2/', views.homepage2,name = 'home2'),


    # path('product-detail/',views.product_all_detail,name= 'product_all_detail'),
    path('product-detail/<int:pk>/',views.product_detail,name= 'product_detail'),
    path('product-detail-affiliate/',views.product_detail_affiliate,name= 'product_detail_affiliate'),
    path('product-detail-variable/',views.product_detail_variable,name= 'product_detail_variable'),

    path('shop-grid-full/', views.shop_grid_full,name = 'shop_grid_full'),
    path('shop-grid-left/<int:pk>/', views.shop_grid_left,name = 'shop_grid_left'),

    path('shop-grid-left/', views.all_shop_grid_left,name = 'all_shop_grid_left'),
    path('shop-grid-left-sub-category/<int:pk>/', views.shop_grid_left_sub_category,name = 'shop_grid_left_sub_category'),
    path('shop-grid-left-category/<int:pk>/', views.shop_grid_left_category,name = 'shop_grid_left_category'),

    path('shop-grid-right/', views.shop_grid_right,name = 'shop_grid_right'),
    path('shop-list-full/', views.shop_list_full,name = 'shop_list_full'),
    path('shop-list-left/', views.shop_list_left,name = 'shop_list_left'),
    path('shop-list-right/', views.shop_list_right,name = 'shop_list_right'),
    path('shop-slide-version2/', views.shop_slider_version2,name = 'shop_slider_version2'),



# all the base file query are been send from here

]
