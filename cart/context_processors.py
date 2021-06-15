from accounting.models import User
from dashboard.models import Address,DefaultAddress,AddressType,Country,State,City,Area,Pincode
from home.models import ProductMainCategory,ProductSubCategory,ProductCategory,MainProduct,Product,Product_SubInformation,Information,ProductTags,ProductPolicy,AvailablePolicies,ProductReview,Product_SubInformation,Information
from wishlist.models import ProductWishList
from cart.models import ProductCart

def c_cart_ProductCart(request):
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

        count = ProductCart.objects.filter(user = request.user).count()
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
        count = {}

    # print('charge',charge)
    # print('total_amount',total_amount)
    # print('gst',gst)
    # print('grandtotal',grand_total)
     
    context = {
        'all_ProductCart' : ProductCarts,
        'all_charge': charges,
        'all_total_amount':total_amount,
        'all_gst': gst,
        'all_grandtotal':grand_total,
        'all_count' : count,
    }

    return context
