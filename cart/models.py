from django.db import models
from accounting.models import User
from dashboard.models import Address,DefaultAddress,AddressType,Country,State,City,Area,Pincode
from home.models import ProductMainCategory,ProductSubCategory,ProductCategory,MainProduct,Product,Product_SubInformation,Information,ProductTags,ProductPolicy,AvailablePolicies,ProductReview,Product_SubInformation,Information
from wishlist.models import ProductWishList
from datetime import datetime
from datetime import date
# Create your models here.



class ProductCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Product_cart_Upload_Date = models.DateTimeField(default = datetime.now())
    Product_quantity = models.IntegerField(default=1,)

    def __str__(self):
        return self.product.Product_Title

