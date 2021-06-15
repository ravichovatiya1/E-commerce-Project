from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.core import serializers
from accounting.models import User
from dashboard.models import Address,DefaultAddress,AddressType,Country,State,City,Area,Pincode
from home.models import ProductMainCategory,ProductSubCategory,ProductCategory,MainProduct,Product,Product_SubInformation,Information,ProductTags,ProductPolicy,AvailablePolicies,ProductReview,Product_SubInformation,Information
from home.forms import ProductUploadForm
from wishlist.models import ProductWishList
from cart.models import ProductCart
from django.contrib import messages
from django.core.files.storage import FileSystemStorage 
from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required
def cart(request):
    total_amount = 0
    gst = 0
    charge = 0
    grand_total = 0
    
    try:
        for product_price in ProductCart.objects.filter(user = request.user):
            total = product_price.product.Product_Price * product_price.Product_quantity
            total_amount += total
            if product_price.product.ProductShipping == 'charge' :
                if total_amount >= 5000 :
                    charge = 0
                else:
                    charge += 75
            else:
                if total_amount >= 5000 :
                    charge = 0
                else :
                    charge += 0

        gst = total_amount/100*17
        total_amount = total_amount/100*83
        grand_total = charge+total_amount+gst
        ProductCarts = ProductCart.objects.filter(user = request.user)

        if grand_total >= 5000:
            charge = 0
        charges = charge

    except:
        gst={}
        total_amount={}
        grand_total={}
        charges={}
        ProductCarts={}

    # print('charge',charge)
    # print('total_amount',total_amount)
    # print('gst',gst)
    # print('grandtotal',grand_total)
     
    context = {
        'ProductCart' : ProductCarts,
        'charge': charges,
        'total_amount':total_amount,
        'gst': gst,
        'grandtotal':grand_total,
    }
        
    return render(request,'cart/cart.html',context)


    

def addCart(request,pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            # print(request.POST.get('product_pk'))
            # print(request.POST.get('product_qty'))
            p, created = ProductCart.objects.get_or_create(
                user = User.objects.get(pk = request.user.pk),
                product = Product.objects.get(pk = pk),
                # Product_quantity = request.POST.get('product_qty'),
            )

            p.Product_quantity = request.POST.get('product_qty')
            p.save()

            if created:
                return JsonResponse({'res':'Product :- Added to cart','qty':request.POST.get('product_qty')})
            else:
                return JsonResponse({'res':'Product :- Exist to cart','qty':request.POST.get('product_qty')})
        else:
            return JsonResponse ({'res':'PleaseLogin'})
    
    return render(request,'cart/cart.html')


def updateCart(request,pk):
    if request.method == 'POST':

        p, created = ProductCart.objects.get_or_create(
            user = User.objects.get(pk = request.user.pk),
            product = Product.objects.get(pk = pk),
            # Product_quantity = request.POST.get('product_qty'),
        )

        p.Product_quantity = request.POST.get('product_qty')
        p.save()

        if created:
            return JsonResponse({'qty':request.POST.get('product_qty')})
        else:
            return JsonResponse({'qty':request.POST.get('product_qty')})
    return render(request,'cart/cart.html')


def wish_to_cart(request,pk):
    if request.method == 'GET':
        p, created = ProductCart.objects.get_or_create(
            user = User.objects.get(pk = request.user.pk),
            product = Product.objects.get(pk = pk),
            # Product_quantity = request.POST.get('product_qty'),
        )
        p.Product_quantity = request.GET.get('product_qty')


        obj_deleted = ProductWishList.objects.filter(product__Product_Title = Product.objects.get(pk = pk)).delete()
        # print(obj_deleted)

        if created:
            return redirect('cart:cart')
        else:
            return redirect('cart:cart')

        
    # wishlist_del = ProductWishList.objects.filter(pk=pk)
    # wishlist_del.delete()
    
    return redirect('cart:cart')

def removeCart(request,pk):
    # print(pk)
    ProductCart.objects.filter(pk=pk).delete()
    return redirect('cart:cart')

def removeAllCart(request):
    try:
        ProductCart.objects.filter(user = User.objects.get(pk = request.user.pk)).delete()
    except:
        messages.error(request,f'login first and try it again..' )
    return redirect('cart:cart')

