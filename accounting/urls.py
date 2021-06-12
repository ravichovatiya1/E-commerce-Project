from django.urls import path,include
from accounting import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

app_name = 'account'

urlpatterns = [
    path('', views.account_information, name = 'account_information'),

    path('signup',views.signup,name = 'signup'),
    path('signup-seller',views.signup_seller,name = 'signup_seller'),
    path('signin/',views.signin,name = 'signin'),
    path('logout/',views.logout_page,name = 'logout'),
    path('lost-password',views.lost_password,name = 'lost_password'),

]



    # path('accounts/', include('allauth.urls')),
    # path('logout', LogoutView.as_view()),