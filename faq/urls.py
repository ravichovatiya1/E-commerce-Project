from django.urls import path,include
from faq import views

app_name ='faq'


urlpatterns = [
        path('',views.faq,name='faq'),

]