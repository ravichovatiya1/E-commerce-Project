from django.contrib import admin
from home import models

# Register your models here.

admin.site.register(models.ProductMainCategory)
admin.site.register(models.ProductSubCategory)
admin.site.register(models.ProductCategory)
admin.site.register(models.MainProduct)
admin.site.register(models.Product)
admin.site.register(models.ProductReview)
admin.site.register(models.Product_SubInformation)
admin.site.register(models.Information)
admin.site.register(models.ProductTags)
admin.site.register(models.ProductPolicy)
admin.site.register(models.AvailablePolicies)


# @admin.register(models.ProductPolicy)
# class ProductPolicyAdminModel(admin.ModelAdmin):
#     list_display = ('pk',)

# @admin.register(models.Information)
# class InformationAdminModel(admin.ModelAdmin):
#     list_display = ('pk',)

