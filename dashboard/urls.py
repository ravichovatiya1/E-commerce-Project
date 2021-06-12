from django.urls import path,include
from dashboard import views

app_name ='profile'

urlpatterns = [
    path('', views.dashboard, name = 'manage_myaccount'),
    path('my-profile',views.myprofile,name = 'myprofile'),
    path('edit-profile',views.edit_profile,name ='edit_profile'),


    path('address-book/',views.address_book,name='address_book'),

    path('edit-address/<int:pk>/',views.edit_address,name='edit_address'),


    path('edit-default-address/',views.edit_default_address, name='edit_default_address'),
    path('add-new-address',views.add_new_address,name='add_new_address'),
    path('track-order',views.track_order,name='track_order'),
    path('my-orders',views.my_orders,name='my_orders'),
    path('manage-orders',views.manage_orders,name='manage_orders'),
    path('my-payment-option',views.my_payment_option,name='my_payment_option'),
    path('track-and-Cancel',views.track_ordMy_Returns_and_Cancellationser,name='trackand_Cancel'),


# all product controles
    path('all-product', views.all_product, name='all_product'),
    path('product-upload', views.product_upload, name='product_upload'), #add product
    path('product-edit/', views.product_edit,name= 'product_edit'),
    path('product-edit-one/<int:pk>/',views.product_edit_one,name='product_edit_one'),
    path('product-edit-delete/<int:pk>/',views.product_edit_delete,name= 'product_edit_delete'),
    path('product-view', views.product_view,name= 'product_view'),
    path('product-view-one/<int:pk>/', views.product_view_one,name= 'product_view_one'),

    
# ajax products categories
    path('get-sub-cat',views.get_sub_cat,name = 'get_sub_cat'),
    path('get-cat',views.get_cat,name = 'get_cat'),
    path('main-product',views.main_product,name = 'main_product'),

# ajax countries
    path('get-state', views.get_state, name = 'get_state'),
    path('get-city', views.get_city, name = 'get_city'),
    path('get-area', views.get_area, name = 'get_area'),
    path('get-pincode', views.get_pincode, name = 'get_pincode'),

]