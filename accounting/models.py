from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User (AbstractUser):
    Mobile = models.IntegerField(null=True,unique=True)
    Dob = models.DateField(null=True)
    Gender = models.CharField(default='male',max_length=20,choices=(('male','male'),('female','female')))
    UserType = models.CharField(default='customer',max_length=20,choices=(('customer','customer'),('seller','seller')))
    email = models.EmailField(unique=True,blank=True, max_length=254, verbose_name='email address')
    

    
    

    # def __str__(self):
    #     return self.username