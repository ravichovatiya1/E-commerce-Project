from django.urls import path,include
from blog import views

app_name ='blog'

urlpatterns = [
        path('',views.blog,name='blog'),# blog-left-sidebar
        path('blog-right-sidebar',views.blog_right_sidebar,name ='blog_right_sidebar'),
        path('blog-sidebar-none',views.blog_sidebar_none,name ='blog_sidebar_none'),
        path('blog-masonry',views.blog_masonry,name ='blog_masonry'),
        path('blog-detail',views.blog_detail,name ='blog_detail'),

]