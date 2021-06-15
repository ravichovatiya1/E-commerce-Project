from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from accounting.models import User
from dashboard.models import Address,DefaultAddress,AddressType,Country,State,City,Area,Pincode
from home.models import ProductMainCategory,ProductSubCategory,ProductCategory,MainProduct,Product,Product_SubInformation,Information,ProductTags,ProductPolicy,AvailablePolicies,ProductReview,Product_SubInformation,Information
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def homepage(request):
    product_wise_stars_count={} # stars counts
    unique_product_rating_count={} # total raters
    review_average = {} # average calculator
    
    for product_name in Product.objects.all():
        temp_sum=0.0
        for product_review in ProductReview.objects.all():
            if product_name.Product_Title == product_review.product.Product_Title:
                temp_sum = temp_sum + float(product_review.Review_Star_Select)
                product_wise_stars_count[product_name.Product_Title] = temp_sum
                # print(product_wise_stars_count)

    for all_product_unique_count in product_wise_stars_count:
        single_product = 0
        for all_product_name in ProductReview.objects.all():
            if all_product_name.product.Product_Title in all_product_unique_count:
                single_product = single_product+1
                unique_product_rating_count[all_product_unique_count]=single_product
                # print(unique_product_rating_count)


    for average_calc in product_wise_stars_count:
        review_average[average_calc] = str(round(product_wise_stars_count[average_calc]/unique_product_rating_count[average_calc]))

    context =  {
        # top tranding filter product sending
        'ProductMainCategory' : ProductMainCategory.objects.all(),
        'ProductSubCategory' : ProductSubCategory.objects.all(),
        'Product':Product.objects.all()[:12],
        'ProductPolicy': ProductPolicy.objects.all(),
        # new arrivals product sending to page
        'na_Product':Product.objects.all().order_by("-Product_Upload_Date")[5:15],
        'na_ProductPolicy': ProductPolicy.objects.all(),
        # FEATURED PRODUCTS sending to page
        'fp_Product':Product.objects.all()[6:10],
        'fp_ProductPolicy': ProductPolicy.objects.all(),
        # SPECIAL PRODUCTS sending to page
        'sp_Product':Product.objects.all()[:3],
        'wp_Product':Product.objects.all()[3:6],
        'flp_Product':Product.objects.all()[6:9],
        'review_average': review_average,
        'unique_product_rating_count':unique_product_rating_count,

    }
    return render(request,'home/index.html',context)


def product_detail(request,pk):
    product_wise_stars_count={} # stars counts
    unique_product_rating_count={} # total raters
    review_average = {} # average calculator
    
    for product_name in Product.objects.all():
        temp_sum=0.0
        for product_review in ProductReview.objects.all():
            if product_name.Product_Title == product_review.product.Product_Title:
                temp_sum = temp_sum + float(product_review.Review_Star_Select)
                product_wise_stars_count[product_name.Product_Title] = temp_sum
                # print(product_wise_stars_count)

    for all_product_unique_count in product_wise_stars_count:
        single_product = 0
        for all_product_name in ProductReview.objects.all():
            if all_product_name.product.Product_Title in all_product_unique_count:
                single_product = single_product+1
                unique_product_rating_count[all_product_unique_count]=single_product
                # print(unique_product_rating_count)


    for average_calc in product_wise_stars_count:
        review_average[average_calc] = str(round(product_wise_stars_count[average_calc]/unique_product_rating_count[average_calc]))
        # print(review_average.sort(reverse=True))


    try:
        user_comment = ProductReview.objects.get(user = request.user, product__pk = pk)
    except:
        user_comment = False
    
    context = {
            'user_detail' : request.user,
            'Product': Product.objects.filter(pk=pk),
            'ProductPolicy': ProductPolicy.objects.all(),
            'ProductReview': ProductReview.objects.filter(product = Product.objects.get(pk=pk)),
            'user_comment' : user_comment,
            'Product_SubInformation' : Product_SubInformation.objects.all(),
            'Information': Information.objects.all(),
            'ProductTags' : ProductTags.objects.all(),
            'review_average': review_average,
            'unique_product_rating_count':unique_product_rating_count,
    }

    if request.method == 'POST':
        try:
            if ProductReview.objects.filter(product = Product.objects.get(pk=pk),user= request.user):
                ProductReview.objects.filter(product = Product.objects.get(pk=pk),user= request.user).update(Review_Star_Select =request.POST.get('rating_get'),Review_Discription = request.POST.get('review_text'),)
                messages.success(request,f'you review is updated' )
                return redirect('home:product_detail',pk=pk)
            else:
                rating = request.POST.get('rating_get')
                discription = request.POST.get('review_text')
                ProductReview.objects.create(
                                            user = User.objects.get(pk = request.user.pk),
                                            product = Product.objects.get(pk = pk),
                                            Review_Star_Select = request.POST.get('rating_get'),
                                            Review_Discription = request.POST.get('review_text'),
                ).save()
                messages.success(request,f'you have add your review')
                return redirect('home:product_detail',pk=pk)

        except:
            messages.success(request,f'Please Login and try it again ...')

    return render(request,'home/product-detail.html',context)

def shop_grid_left(request,pk):
    product_wise_stars_count={} # stars counts
    unique_product_rating_count={} # total raters
    review_average = {} # average calculator
    
    for product_name in Product.objects.all():
        temp_sum=0.0
        for product_review in ProductReview.objects.all():
            if product_name.Product_Title == product_review.product.Product_Title:
                temp_sum = temp_sum + float(product_review.Review_Star_Select)
                product_wise_stars_count[product_name.Product_Title] = temp_sum
                # print(product_wise_stars_count)

    for all_product_unique_count in product_wise_stars_count:
        single_product = 0
        for all_product_name in ProductReview.objects.all():
            if all_product_name.product.Product_Title in all_product_unique_count:
                single_product = single_product+1
                unique_product_rating_count[all_product_unique_count]=single_product
                # print(unique_product_rating_count)


    for average_calc in product_wise_stars_count:
        review_average[average_calc] = str(round(product_wise_stars_count[average_calc]/unique_product_rating_count[average_calc]))


    ################################################################################################
    Product_paginations = Product.objects.filter(maincategory = ProductMainCategory.objects.get(pk=pk))

    paginator = Paginator(Product_paginations,3)  # 5 content per page

    page = request.GET.get('page',1)

    try:
        Product_pagination = paginator.page(page)
    except PageNotAnInteger:
        Product_pagination = paginator.page(1)
    except EmptyPage:
        Product_pagination = paginator.page(paginator.num_pages)


    context =  {
        'ProductSubCategory' : ProductSubCategory.objects.all(),
        'Product':Product_pagination,
        'review_average': review_average,
        'unique_product_rating_count':unique_product_rating_count,
        'ProductPolicy': ProductPolicy.objects.all(),

    }
    return render(request,'home/shop-grid-left.html',context)
    
def all_shop_grid_left(request):

    product_wise_stars_count={} # stars counts
    unique_product_rating_count={} # total raters
    review_average = {} # average calculator
    
    for product_name in Product.objects.all():
        temp_sum=0.0
        for product_review in ProductReview.objects.all():
            if product_name.Product_Title == product_review.product.Product_Title:
                temp_sum = temp_sum + float(product_review.Review_Star_Select)
                product_wise_stars_count[product_name.Product_Title] = temp_sum
                # print(product_wise_stars_count)

    for all_product_unique_count in product_wise_stars_count:
        single_product = 0
        for all_product_name in ProductReview.objects.all():
            if all_product_name.product.Product_Title in all_product_unique_count:
                single_product = single_product+1
                unique_product_rating_count[all_product_unique_count]=single_product
                # print(unique_product_rating_count)


    for average_calc in product_wise_stars_count:
        review_average[average_calc] = str(round(product_wise_stars_count[average_calc]/unique_product_rating_count[average_calc]))


    #####################################################################
    Product_paginations = Product.objects.all().order_by("-Product_Upload_Date")

    number_from_ajax_coming = request.GET.get('pg_per_pro_passed') # ex:1,2,3,4
    # print(number_from_ajax_coming)
    paginator = Paginator(Product_paginations,5)  # 5 content per page

    page = request.GET.get('page',1)

    try:
        Product_pagination = paginator.page(page)
    except PageNotAnInteger:
        Product_pagination = paginator.page(1)
    except EmptyPage:
        Product_pagination = paginator.page(paginator.num_pages)

    context =  {
        'ProductSubCategory' : ProductSubCategory.objects.all(),
        'Product':Product_pagination,
        'review_average': review_average,
        'unique_product_rating_count':unique_product_rating_count,
        'ProductPolicy': ProductPolicy.objects.all(),
    }


    return render(request,'home/shop-grid-left.html',context)

def shop_grid_left_sub_category(request,pk):
    
    product_wise_stars_count={} # stars counts
    unique_product_rating_count={} # total raters
    review_average = {} # average calculator
    
    for product_name in Product.objects.all():
        temp_sum=0.0
        for product_review in ProductReview.objects.all():
            if product_name.Product_Title == product_review.product.Product_Title:
                temp_sum = temp_sum + float(product_review.Review_Star_Select)
                product_wise_stars_count[product_name.Product_Title] = temp_sum
                # print(product_wise_stars_count)

    for all_product_unique_count in product_wise_stars_count:
        single_product = 0
        for all_product_name in ProductReview.objects.all():
            if all_product_name.product.Product_Title in all_product_unique_count:
                single_product = single_product+1
                unique_product_rating_count[all_product_unique_count]=single_product
                # print(unique_product_rating_count)


    for average_calc in product_wise_stars_count:
        review_average[average_calc] = str(round(product_wise_stars_count[average_calc]/unique_product_rating_count[average_calc]))
    
    ##################################################################################################
    Product_paginations = Product.objects.filter(subcategory = ProductSubCategory.objects.get(pk=pk))

    paginator = Paginator(Product_paginations,5)  # 5 content per page

    page = request.GET.get('page',1)

    try:
        Product_pagination = paginator.page(page)
    except PageNotAnInteger:
        Product_pagination = paginator.page(1)
    except EmptyPage:
        Product_pagination = paginator.page(paginator.num_pages)

    context =  {
        'ProductSubCategory' : ProductSubCategory.objects.all(),
        'Product':Product_pagination,
        'review_average': review_average,
        'unique_product_rating_count':unique_product_rating_count,
        'ProductPolicy': ProductPolicy.objects.all(),

    }
    return render(request,'home/shop-grid-left.html',context)


def shop_grid_left_category(request,pk):
    
    product_wise_stars_count={} # stars counts
    unique_product_rating_count={} # total raters
    review_average = {} # average calculator
    
    for product_name in Product.objects.all():
        temp_sum=0.0
        for product_review in ProductReview.objects.all():
            if product_name.Product_Title == product_review.product.Product_Title:
                temp_sum = temp_sum + float(product_review.Review_Star_Select)
                product_wise_stars_count[product_name.Product_Title] = temp_sum
                # print(product_wise_stars_count)

    for all_product_unique_count in product_wise_stars_count:
        single_product = 0
        for all_product_name in ProductReview.objects.all():
            if all_product_name.product.Product_Title in all_product_unique_count:
                single_product = single_product+1
                unique_product_rating_count[all_product_unique_count]=single_product
                # print(unique_product_rating_count)


    for average_calc in product_wise_stars_count:
        review_average[average_calc] = str(round(product_wise_stars_count[average_calc]/unique_product_rating_count[average_calc]))

    ##################################################################################################
    Product_paginations = Product.objects.filter(category = ProductCategory.objects.get(pk=pk))

    paginator = Paginator(Product_paginations,5)  # 5 content per page

    page = request.GET.get('page',1)

    try:
        Product_pagination = paginator.page(page)
    except PageNotAnInteger:
        Product_pagination = paginator.page(1)
    except EmptyPage:
        Product_pagination = paginator.page(paginator.num_pages)


    context =  {
        'ProductSubCategory' : ProductSubCategory.objects.all(),
        'Product':Product_pagination,
        'review_average': review_average,
        'unique_product_rating_count':unique_product_rating_count,
        'ProductPolicy': ProductPolicy.objects.all(),

    }
    return render(request,'home/shop-grid-left.html',context)

