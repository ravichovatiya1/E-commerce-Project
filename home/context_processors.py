from home.models import ProductMainCategory,ProductSubCategory,ProductCategory,MainProduct,Product,Product_SubInformation,Information,ProductTags,ProductPolicy,AvailablePolicies,ProductReview,Product_SubInformation,Information

def c_ProductMainCategory(request):
    context={}
    all_ProductMainCategory = ProductMainCategory.objects.all()
    context['all_ProductMainCategory']=all_ProductMainCategory

    all_ProductSubCategory = ProductSubCategory.objects.all()
    context['all_ProductSubCategory']=all_ProductSubCategory

    all_ProductCategory = ProductCategory.objects.all()
    context['all_ProductCategory']=all_ProductCategory

    return context
