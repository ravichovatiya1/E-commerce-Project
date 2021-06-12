from django.contrib import admin
from dashboard import models

# Register your models here.
admin.site.register(models.AddressType)
admin.site.register(models.Address)
admin.site.register(models.Country)
admin.site.register(models.State)
admin.site.register(models.City)
admin.site.register(models.Area)
admin.site.register(models.Pincode)
admin.site.register(models.DefaultAddress)

