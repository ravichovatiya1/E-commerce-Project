from django.db import models
from home.models import ProductMainCategory,ProductSubCategory,ProductCategory,MainProduct,Product,Product_SubInformation,Information,ProductTags,ProductPolicy,AvailablePolicies,ProductReview,Product_SubInformation,Information
from django import forms

class ProductUploadForm(forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        exclude= ('Product_Upload_Date','user')