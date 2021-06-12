from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect 
from django.contrib.auth import authenticate,login,logout
# from account.models import MyUser
from django.contrib import messages
from django.urls import reverse  #this is for reversee file top and this at once 
from django.contrib.auth import get_user_model   #to enter user datta in user models 
MyUser = get_user_model() 

# Create your views here.

def account_information(request):
    return render(request,'dashboard/dashboard.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password1')

        first_four = contact[:4]
        email_split = email.split('@')[0]
        username = email_split + str(first_four)
        try:
            MyUser.objects.get(Mobile=contact)
            messages.error(request,'mobile no is already taken')
            return render(request,'account/customer/signup.html')
        except:
            try:
                MyUser.objects.get(email=email)
                messages.error(request,'email is already taken please Signin again')
                return render(request,'account/customer/signup.html')
            except:
                MyUser.objects.create_user(username=username,email=email,first_name =first_name ,last_name=last_name ,Mobile=contact,password=password,Gender=gender,Dob=dob)
                messages.success(request,f'your regestration is sucessfull hello " {username} ", you are welcome')
                return HttpResponseRedirect(reverse('account:signin'))
    else:
        return render(request,'account/customer/signup.html')


def signup_seller(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password1')

        first_four = contact[:4]
        email_split = email.split('@')[0]
        username = email_split + str(first_four)
        try:
            MyUser.objects.get(Mobile=contact)
            messages.error(request,'mobile no is already taken')
            return render(request,'account/seller/signup.html')
        except:
            try:
                MyUser.objects.get(email=email)
                messages.error(request,'email is already taken')
                return render(request,'account/seller/signup.html')
            except:
                MyUser.objects.create_user(username=username,email=email,first_name =first_name ,last_name=last_name ,Mobile=contact,password=password,Gender=gender,Dob=dob,UserType='seller')
                messages.success(request,f'your seller regestration is sucessfull hello " {username} ", you are welcome')
                return HttpResponseRedirect(reverse('account:signin'))
    else:
        return render(request,'account/seller/seller-signup.html')

def signin(request):
    if request.method =="POST":
        username = request.POST.get('email_user')
        password = request.POST.get('passwords')
        try:
            login_user = authenticate(username=MyUser.objects.get(email=username),password=password)
        except:
            login_user = authenticate(username=username,password=password)
        if login_user :
            login(request,login_user)
            if request.user.UserType == 'customer':
                messages.success(request,'Login Sucessfull customer')
                return redirect('home:home')
            elif request.user.UserType == 'seller':
                messages.success(request,'Login Sucessfull seller ')
                return redirect('home:home')
            else:
                messages.success(request,'Login Sucessfull else part')
                return redirect('home:home')
        else:
            messages.error(request,'Invalid Credentionals')
            return render(request,'account/signin.html')   
    else:
        return render(request,'account/signin.html')


# this is for the password reset done in projects.urls files with url 'accounts/login/'
def redirectToLogin(request):
    return redirect('account:signin')

def logout_page(request):
    logout(request)
    return redirect('account:signin')


def lost_password(request):
    return render(request,'registration/password_reset.html')
