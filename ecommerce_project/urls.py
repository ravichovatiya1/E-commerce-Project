"""ecommerce_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from django.contrib.auth import views as auth_views
from accounting import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/login/', views.redirectToLogin, name='login'),
    path('admin/', admin.site.urls),
    path('account/', include('accounting.urls')),
    path('accounts/', include('allauth.urls')),
    path('account/signup/', TemplateView.as_view(template_name="account/customer/signup.html")),

    path('', include('home.urls')),
    path('profile/', include('dashboard.urls')),
    path('cart/', include('cart.urls')),
    path('blog/', include('blog.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('faq/', include('faq.urls')),
    path('about/', include('about_us.urls')),
    path('contact/', include('contact.urls')),
    path('checkout/', include('checkout.urls')),

    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name = "registration/password_reset.html"),name='lost_password'),
    path('accounts/', include('django.contrib.auth.urls')),

]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
