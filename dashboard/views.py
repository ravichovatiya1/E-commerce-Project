from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.core import serializers
from accounting.models import User
from dashboard.models import Address,DefaultAddress,AddressType,Country,State,City,Area,Pincode
from home.models import ProductMainCategory,ProductSubCategory,ProductCategory,MainProduct,Product,Product_SubInformation,Information,ProductTags,ProductPolicy,AvailablePolicies,ProductReview,Product_SubInformation,Information
from home.forms import ProductUploadForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage 

# from django.contrib.auth import get_user_model   #to enter user datta in user models 
# User = get_user_model() 


# Create your views here.

def dashboard(request):
    try :
        user_default_address = DefaultAddress.objects.get(user= request.user)
    except:
        user_default_address = 'add default address for shifting'

    context =  {
            'user_detail' : request.user,
            # 'user_default_address' : DefaultAddress.objects.get(user= request.user),
            'user_default_address': user_default_address
    }
    return render(request,'dashboard/dashboard.html',context)

def myprofile(request):
    context =  {
            'user_detail' : request.user
    }

    return render(request,'dashboard/dash-my-profile.html',context)

def edit_profile(request):
    
    if request.method == 'POST':
        user_data = User.objects.filter(pk = request.user.id).update(first_name = request.POST.get('add_fname'),
                                                                 last_name = request.POST.get('add_lname'), 
                                                                 Dob = request.POST.get('date_of_birth'), 
                                                                 Gender = request.POST.get('add_gender'), 
                                                                 email = request.POST.get('add_email'), 
                                                                 Mobile = request.POST.get('add_contact'))
        messages.success(request,f'your profile is updated please refresh the page')
        redirect('profile:manage_myaccount')
    else:
        if request.method == 'POST':
            # taken_email = request.POST.get('add_email')
            # check_email = User.objects.get(email=taken_email)
            # print(check_email)
            # messages.error(request,f'your eamil is already taken')
            messages.error(request,f'your profile is not updated please try again')

    context =  {
            'user_detail' : request.user
        }
    return render(request,'dashboard/dash-edit-profile.html',context)


def address_book(request):
    context =  {
            'user_detail' : request.user,
            'user_addresses' : Address.objects.filter(user = request.user),
    }
    return render (request,'dashboard/dash-address-book.html',context)


def edit_address(request,pk):
    if request.method == 'POST':
        # print(pk)
        # print(Address.objects.filter(pk = pk))
        Address.objects.filter(pk=pk).update(
                                                user = request.user,
                                                FirstName = request.POST.get('FirstName'),
                                                LastName = request.POST.get('LastName'),
                                                Contact = request.POST.get('Contact'),
                                                StreetAddress = request.POST.get('Street_Address'),
                                                country = request.POST.get('Country'),
                                                state = request.POST.get('State'),
                                                area = request.POST.get('Area'),
                                                address_type = request.POST.get('Address_Type'),
                                                city = request.POST.get('City'),
                                                pincode = request.POST.get('pin_Code'),
                                            )
        messages.success(request,f'your address profile is currently updated')


    context =  {
            'user_detail' : request.user,
            'user_addresses' : Address.objects.filter(pk=pk),
            'countrys' : Country.objects.all(),
            'states' : State.objects.all() , 
            'citys' : City.objects.all(),
            'areas' : Area.objects.all(),
            'pincodes' : Pincode.objects.all(),
            'address_types' : AddressType.objects.all(),
    }
    return render (request,'dashboard/dash-address-edit.html',context)


def edit_default_address(request):
    if request.method == 'POST':
        used_deflt_id = request.POST.get('default_address')
        user_set = Address.objects.get(pk = used_deflt_id)
        try:
            DefaultAddress.objects.filter(user=request.user).update(dafault_address=user_set)
            print("try")

        except:
            DefaultAddress.objects.create(user=request.user,dafault_address=user_set)
            print("except")
        

    context =  {
                'user_detail' : request.user,
                'user_addresses' : Address.objects.filter(user=request.user),
                'user_default_address' : DefaultAddress.objects.get(user=request.user),
        }
    return render(request,'dashboard/dash-address-make-default.html',context)




def add_new_address(request):
    if request.method == 'POST':
        # print(pk)
        obj = Address.objects.create(
                                    user = request.user,
                                    FirstName = request.POST.get('FirstName'),
                                    LastName = request.POST.get('LastName'),
                                    Contact = request.POST.get('New_Contact'),
                                    StreetAddress = request.POST.get('New_Street_Address'),
                                    country = Country.objects.get(pk= request.POST.get('New_country')),
                                    state = State.objects.get(pk = request.POST.get('New_State')),
                                    area = Area.objects.get(pk= request.POST.get('New_Area')),
                                    address_type = AddressType.objects.get(pk=request.POST.get('New_Address_Type')),
                                    city = City.objects.get(pk=request.POST.get('New_City')),
                                    pincode =Pincode.objects.get(pk= request.POST.get('New_Pincode')),
                                    )
        obj.save()
        messages.success(request,f'your address profile created')
        print(obj.pk)

        try:
            efault_user_obj = DefaultAddress.objects.get(user = request.user)
        except:
            deflt_obj = DefaultAddress.objects.create(user= request.user,dafault_address = Address.objects.get(pk=obj.pk))
            deflt_obj.save()
            

    context =  {
            'user_detail' : request.user,
            'countrys' : Country.objects.all(),
            'states' : State.objects.all() , 
            'citys' : City.objects.all(),
            'areas' : Area.objects.all(),
            'pincodes' : Pincode.objects.all(),
            'address_types' : AddressType.objects.all(),
            # 'add_address' : Address.objects.get(user= request.user)
    }
    # print(Country)
    return render(request,'dashboard/dash-address-add.html',context)

def track_order(request):
    context =  {
            'user_detail' : request.user
    }
    return render (request,'dashboard/dash-track-order.html',context)

def my_orders(request):
    context =  {
            'user_detail' : request.user
    }
    return render (request,'dashboard/dash-my-order.html',context)

def manage_orders(request):
    context =  {
            'user_detail' : request.user
    }
    return render(request,'dashboard/dash-manage-order.html',context)

def my_payment_option(request):
    context =  {
            'user_detail' : request.user
    }
    return render (request,'dashboard/dash-payment-option.html',context)

def track_ordMy_Returns_and_Cancellationser(request):
    context =  {
            'user_detail' : request.user
    }
    return render (request,'dashboard/dash-cancellation.html',context)


def all_product(request):
    context =  {
            'user_detail' : request.user
    }
    return render(request,'dashboard/dash-product-index.html',context)


def product_upload(request):
    context =  {
            'user_detail' : request.user,
            'ProductMainCategory' : ProductMainCategory.objects.all(),
            'ProductSubCategory' : ProductSubCategory.objects.all(),
            'ProductCategory' : ProductCategory.objects.all(),
            'MainProduct' : MainProduct.objects.all(),
            'AvailablePolicies' : AvailablePolicies.objects.all(), 
            # 'form': form,
        }
    
    if request.method == 'POST':

        # this is to pass the form and recive the request.post of product
        form = ProductUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = User.objects.get(pk=request.user.pk)
            form_obj.save()


            # this is the code of product selected policies
            policy_id = request.POST.get('allpolicy')
            policy_id = policy_id.split(',')
            select_name_of_policy =[]
            for policy in policy_id:
                policy = int(policy)-1
                name = AvailablePolicies.objects.all()
                select_name_of_policy.append(name[policy])  
                print(select_name_of_policy)
            
            for add_policy in select_name_of_policy:
                add_q = str(add_policy)
                print(add_q)
                policy_obj = ProductPolicy.objects.create(product = Product.objects.get(pk= form_obj.pk),
                                                        Product_Policy = add_q)


            # this is of the product informations
            ProductInfo_Q = request.POST.getlist('ProductInfo_Q')
            ProductInfo_A = request.POST.getlist('ProductInfo_A')

            question  = ProductInfo_Q
            answer = ProductInfo_A
            questions=[]
            answers=[]
            for cap_Que in range(len(question)):
                cap_Que1 = question[cap_Que].capitalize()
                cap_Ans1 = answer[cap_Que].capitalize()
                cap_Que2 = " ".join(cap_Que1.split())
                cap_Ans2 = " ".join(cap_Ans1.split())
                questions.append(cap_Que2)
                answers.append(cap_Ans2)
            print(questions)
            print(answers)  

            dict={}
            for Que in range(len(questions)):
                if questions[Que] not in dict:
                    dict[questions[Que]] = []
                    dict[questions[Que]].append(answers[Que])
                else:
                    dict[questions[Que]].append(answers[Que])
            print(dict)


            for Dic in dict:
                print('question',Dic)
                sub_que = Product_SubInformation.objects.create(product = Product.objects.get(pk= form_obj.pk),Product_Sub_Information = Dic)
                sub_que.save()
                print(sub_que)
                for Ans in range(len(dict[Dic])):
                    # Information.product_subInformation = sub_que.Product_Sub_Information
                    # Information.options = dict[Dic][Ans]
                    # Information.save()
                    info_option = Information.objects.create(product_subInformation = sub_que,options = dict[Dic][Ans]).save()
                    print('answer',dict[Dic][Ans])

            # this is for the product review
            ProductReview.objects.create(
                                            user = User.objects.get(pk = request.user.pk),
                                            product = Product.objects.get(pk=form_obj.pk),
                                            Review_Star_Select = '1.0',
                                            Review_Discription = f'this product name by "{form_obj.Product_Title}"  is upload by "{request.user}" it is the first comment of the user he can edit the comment later'
            ).save()


            # this is for the product tags
            ProductTags.objects.create(
                                            product = Product.objects.get(pk=form_obj.pk),
                                            Product_Tags = request.POST.get('Product_Tags')
            ).save()

            policy_obj.save()
            return HttpResponse('form saved')
        else:
            print(form.errors)
            return HttpResponse('form not saved')


    return render (request,'dashboard/dash-product-upload.html',context)



def product_edit(request):
    context =  {
            'user_detail' : request.user,
            'Product' : Product.objects.filter(user = request.user.id)
    }
    return render(request,'dashboard/dash-product-edit.html',context)


def product_edit_one(request,pk):
    # if request.method == "GET":
        # print(ProductPolicy.objects.filter(product = pk))


    context =  {
            'user_detail' : request.user,
            'ProductMainCategory' : ProductMainCategory.objects.all(),
            'ProductSubCategory' : ProductSubCategory.objects.all(),
            'ProductCategory' : ProductCategory.objects.all(),
            'Product' : Product.objects.filter(pk=pk),
            'MainProduct' : MainProduct.objects.all(),
            'AvailablePolicies' : AvailablePolicies.objects.all(),
            'ProductPolicy' :ProductPolicy.objects.filter(product=pk),
            'ProductTags' : ProductTags.objects.filter(product=pk),

        }
    if request.method=='POST':
        get_obj = get_object_or_404(Product,pk=pk)
        form = ProductUploadForm(request.POST or None,request.FILES, instance=get_obj)
        if form.is_valid():
            form_obj =form.save()
            print(form_obj.pk)

            # this is to update the product tags
            ProductTags.objects.update(
                                        product = form_obj,
                                        Product_Tags = request.POST.get('Product_Tags')
            )

            # ProductTags.objects.filter(product = pk).update(
            #                             Product_Tags = request.POST.get('Product_Tags')
            # )

            # this is to update the policy of user
            policy_id = request.POST.get('allpolicy')
            # print(policy_id)
            policy_id = policy_id.split(',')
            select_name_of_policy =[]
            for policy in policy_id:
                policy = int(policy)-1
                # print(policy)
                name = AvailablePolicies.objects.all()
                select_name_of_policy.append(name[policy])  
                # print(select_name_of_policy)
            
            list_add_q =[]
            for add_policy in select_name_of_policy:
                add_q = str(add_policy)
                print('all_selected',add_q)
                list_add_q.append(add_q)

            for before_policies in ProductPolicy.objects.filter(product = pk):
                before_policies = str(before_policies)
                print('befor policies',before_policies)

                # print(add_q)
            #     policy_obj = ProductPolicy.objects.create(product = Product.objects.get(pk= form_obj.pk),
            #                                             Product_Policy = add_q)
            # policy_obj.save()
                # print()

            
            

            return HttpResponse('form saved')
        # print(request.POST.get('Product_Title'))
    return render(request,'dashboard/dash-product-edit-one.html',context) 

def product_edit_delete(request,pk):
    Product.objects.filter(pk=pk).delete()
    return redirect('profile:product_edit')


def product_view(request):
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

    # print(review_average)
    # print(product_wise_stars_count)
    # print(unique_product_rating_count)



    context =  {
            'user_detail' : request.user,
            'ProductMainCategory' : ProductMainCategory.objects.all(),
            'ProductSubCategory' : ProductSubCategory.objects.all(),
            'ProductCategory' : ProductCategory.objects.all(),
            'MainProduct' : MainProduct.objects.all(),
            'AvailablePolicies' : AvailablePolicies.objects.all(), 
            'Product': Product.objects.all(),
            'ProductPolicy': ProductPolicy.objects.all(),
            'ProductReview': ProductReview.objects.all(),
            'review_average': review_average,
            'unique_product_rating_count':unique_product_rating_count,
    }
    return render(request,'dashboard/dash-product-view.html',context)


def product_view_one(request,pk):

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

    context = {
            'user_detail' : request.user,
            'ProductMainCategory' : ProductMainCategory.objects.all(),
            'ProductSubCategory' : ProductSubCategory.objects.all(),
            'ProductCategory' : ProductCategory.objects.all(),
            'MainProduct' : MainProduct.objects.all(),
            'AvailablePolicies' : AvailablePolicies.objects.all(), 
            'Product': Product.objects.filter(pk=pk),
            'ProductPolicy': ProductPolicy.objects.all(),
            'ProductReview': ProductReview.objects.all(),
            'Product_SubInformation' : Product_SubInformation.objects.all(),
            'Information': Information.objects.all(),
            'ProductTags' : ProductTags.objects.all(),
            'review_average':review_average,
            'unique_product_rating_count':unique_product_rating_count,
    }
    return render(request,'dashboard/dash-product-view-one.html',context)











# this is of the ajax for the product selection
def get_sub_cat(request):
    p_main_category_cat_id = request.GET.get('p_main_category')
    i_id_p_main_category = ProductMainCategory.objects.get(pk = p_main_category_cat_id)
    sub_filters = ProductSubCategory.objects.filter(maincategory = i_id_p_main_category)
    return JsonResponse(serializers.serialize('json',sub_filters),safe=False)



def get_cat(request):
    p_sub_category_cat_id = request.GET.get('p_sub_category')
    cat_filters = ProductCategory.objects.filter(subcategory = int(p_sub_category_cat_id))
    return JsonResponse(serializers.serialize('json',cat_filters),safe=False)


def main_product(request):
    p_main_product_cat_id = request.GET.get('p_category')
    main_pro_filters = MainProduct.objects.filter(productcategory = int(p_main_product_cat_id))
    return JsonResponse(serializers.serialize('json',main_pro_filters),safe=False)
    # return HttpResponse('this is the sample')



# this is the ajax of country

def get_state(request):
    country_id = request.GET.get('new_add_country')
    # print(country_id)
    i_id_country = Country.objects.get(pk = country_id)
    # print(i_id_country)
    sub_states = State.objects.filter(country = i_id_country)
    # print(sub_states)
    return JsonResponse(serializers.serialize('json',sub_states),safe=False)
    # return HttpResponse('this is to select the states')

def get_city(request):
    state_id = request.GET.get('new_add_state')
    # print(state_id)
    i_id_state = State.objects.get(pk = state_id)
    # print(i_id_country)
    sub_city = City.objects.filter(state = i_id_state)
    # print(sub_states)
    return JsonResponse(serializers.serialize('json',sub_city),safe=False)
    # return HttpResponse('this is to select the states')

def get_area (request):
    city_id = request.GET.get('new_add_city')
    # print(city_id)
    i_id_city = City.objects.get(pk = city_id)
    # print(i_id_city)
    sub_area = Area.objects.filter(city = i_id_city)
    # print(sub_area)
    return JsonResponse(serializers.serialize('json',sub_area),safe=False)
    # return HttpResponse('this is to select the states')

def get_pincode(request):
    area_id = request.GET.get('new_add_area')
    # print(area_id)
    i_id_area = Area.objects.get(pk = area_id)
    # print(i_id_area)
    sub_pincode = Pincode.objects.filter(area = i_id_area)
    # print(sub_pincode)
    return JsonResponse(serializers.serialize('json',sub_pincode),safe=False)
    # return HttpResponse('this is to select the states')
    
