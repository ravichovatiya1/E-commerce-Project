from django.db import models
from accounting.models import User
from django.urls import reverse

# Create your models here.

class AddressType(models.Model):
    Types = models.CharField(default='home',max_length=20,choices=(('home','home'),('office','office')))

    def __str__(self):
        return self.Types

class Country(models.Model):
    CountryName = models.CharField(max_length=256)

    def __str__(self):
        return self.CountryName

class State(models.Model):
    StateName = models.CharField(max_length=40)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.StateName

class City(models.Model):
    CityName = models.CharField(max_length=40)
    state = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.CityName

class Area(models.Model):
    AreaName = models.CharField(max_length=40)
    city = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.AreaName


class Pincode(models.Model):
    PincodeArea = models.CharField(max_length=40)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)

    def __str__(self):
        return self.PincodeArea

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=256)
    LastName = models.CharField(max_length=256)
    Contact = models.IntegerField()
    address_type = models.ForeignKey(AddressType,on_delete=models.CASCADE)# 
    StreetAddress = models.CharField(max_length=256)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)#
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    pincode = models.ForeignKey(Pincode,on_delete=models.CASCADE)


    # def get_absolute_url(self):
    #     return reverse("profile:editAddress", kwargs={"pk": self.pk})

    def __str__(self):
        return self.user.first_name +' '+self.user.last_name +' -> '+ self.StreetAddress

class DefaultAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    dafault_address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name +' '+self.user.last_name +' -> '+ self.dafault_address.StreetAddress








    
