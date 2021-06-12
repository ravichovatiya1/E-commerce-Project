from django.urls import path,include
from about_us import views

app_name = 'about'

urlpatterns = [
        path('',views.about,name='about_us'),


]