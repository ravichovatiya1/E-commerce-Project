from django.shortcuts import render



# Create your views here.

def blog(request):
    return render(request,'blog/blog-left-sidebar.html')

def blog_right_sidebar(request):
    return render(request,'blog/blog-right-sidebar.html')

def blog_sidebar_none(request):
    return render(request,'blog/blog-sidebar-none.html')

def blog_masonry(request):
    return render(request,'blog/blog-masonry.html')

def blog_detail(request):
    return render(request,'blog/blog-detail.html')



