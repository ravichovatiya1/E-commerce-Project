from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.core import serializers
from accounting.models import User
from dashboard.models import Address,DefaultAddress,AddressType,Country,State,City,Area,Pincode
from home.models import ProductMainCategory,ProductSubCategory,ProductCategory,MainProduct,Product,Product_SubInformation,Information,ProductTags,ProductPolicy,AvailablePolicies,ProductReview,Product_SubInformation,Information
from home.forms import ProductUploadForm
from wishlist.models import ProductWishList
from django.contrib import messages
from django.core.files.storage import FileSystemStorage 
# from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required
def wishlist(request):
    # print(ProductWishList.objects.filter(user = request.user))
    try:
        user_wishlist = ProductWishList.objects.filter(user = request.user)
    except:
        user_wishlist ={}
    
    context = {
            'ProductWishList' : user_wishlist,
        }

    return render(request,'wishlist/wishlist.html',context)
    

def addWish(request,pk):
    if request.method == 'POST':
        # print(request.POST.get('product_pk'))
        
        # ProductWishList.objects.create(
        #     user = User.objects.get(pk = request.user.pk),
        #     product = Product.objects.get(pk = request.POST.get('product_pk'))
        # ).save()
        # print(pk)

        p, created = ProductWishList.objects.get_or_create(
            user = User.objects.get(pk = request.user.pk),
            product = Product.objects.get(pk = pk)
        )

        if created:
            return JsonResponse({'res':'Product is Added to Wishlist'})
        else:
            return JsonResponse({'res':'Product is Exist to Wishlist'})

    return render(request,'wishlist/wishlist.html')


def removeWish(request,pk):
    print(pk)
    # if ProductWishList == request.user:
    ProductWishList.objects.filter(pk=pk).delete()
    return redirect('wishlist:wishlist')
    # else:
        # HttpResponse('please login with the correct user and try again')
    # return render(request,'wishlist/wishlist.html')

def removeAllWish(request):
    try:
        ProductWishList.objects.filter(user = User.objects.get(pk = request.user.pk)).delete()
    except:
        messages.error(request,f'login first and try it again..' )
    return redirect('wishlist:wishlist')
