

# this is for the product to take of electronics
# https://www.bhphotovideo.com/c/product/1296081-REG/makerbot_mp07825_replicator_3d_printer.html?gclid=CjwKCAjwnPOEBhA0EiwA609ReViNf_xylBaIaEjkjQ9VkxB2Mte5wKeN4isUZGjjLY4VvAxoRtNNfhoCUTEQAvD_BwE

from django.db import models
from datetime import datetime
from datetime import date
from django.db.models.base import Model
from PIL import Image # this is to reduce the size of the images in Product.
from django.db.models.fields import CharField
from accounting.models import User

# Create your models here.



################################################################################################3
class ProductMainCategory(models.Model):
    Main_Category = models.CharField(max_length=256)

    def __str__(self):
        return self.Main_Category

class ProductSubCategory(models.Model):
    maincategory = models.ForeignKey(ProductMainCategory,on_delete=models.CASCADE)
    Sub_Category = models.CharField(max_length=256)

    def __str__(self):
        # return self.maincategory.Main_Category+ ' -> ' + self.Sub_Category
        return self.Sub_Category

class ProductCategory(models.Model):
    subcategory = models.ForeignKey(ProductSubCategory,on_delete=models.CASCADE)
    Category = models.CharField(max_length=256)

    def __str__(self):
        # return self.subcategory.maincategory.Main_Category+ ' -> ' + self.subcategory.Sub_Category + ' -> ' + self.Category
        return self.Category


class MainProduct(models.Model):
    productcategory = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    Main_Product = models.CharField(max_length=256)

    def __str__(self):
        # return self.productcategory.subcategory.Sub_Category + ' -> ' + self.productcategory.Category + ' -> ' +self.Main_Product
        return self.Main_Product



def img_path(instance, filename):
    dates = date.today().strftime('%Y/%m/%d') 
    path = f'products/{instance.user.username}/{dates}/product_{instance.id}/{filename}'
    return path

class Product(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,null=True)
    maincategory = models.ForeignKey(ProductMainCategory,on_delete=models.CASCADE,null=True)
    subcategory = models.ForeignKey(ProductSubCategory,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,null=True)
    mainproduct = models.ForeignKey(MainProduct, on_delete = models.CASCADE,null=True)
    Product_Img_1 = models.ImageField(upload_to=img_path,null=True)
    Product_Img_2 = models.ImageField(upload_to=img_path,null=True)
    Product_Img_3 = models.ImageField(upload_to=img_path,null=True)
    Product_Img_4 = models.ImageField(upload_to=img_path,null=True)
    Product_Img_5 = models.ImageField(upload_to=img_path,null=True)
    Product_Upload_Date = models.DateTimeField(default = datetime.now(),null=True)
    Product_Title = models.CharField(max_length = 256,null=True)
    Product_Price = models.FloatField(null=True)
    Product_Percentage_Off = models.FloatField(null=True)
    Product_Cutoff_Price = models.FloatField(null=True)
    Product_Disc = models.CharField(max_length=50000,null=True)
    Product_Stock = models.IntegerField(default=1,null=True)
    Product_Weight = models.FloatField(null=True)
    Product_Warrenty = models.FloatField(default= 1.0 ,null=True)
    Product_Garenty = models.FloatField(default= 1.0,null=True )
    ProductShipping = models.CharField(max_length=256,default = 'charge',choices= (('charge','charge'),('free','free')),null=True)

    def save(self, *args, **kwrgs):
        super().save(*args,**kwrgs)

# https://stackoverflow.com/questions/23921745/pillow-resize-pixelating-images-django-pillow

        large_size1 = (1600, 1600)
        im1 = Image.open(self.Product_Img_1.path)
        image_w1, image_h1 = im1.size
        aspect_ratio1 = image_w1 / float(image_h1)
        new_height1 = int(large_size1[0] / aspect_ratio1)
        if new_height1 < 1600:
            final_width1 = large_size1[0]
            final_height1 = new_height1
        else:
            final_width1 = int(aspect_ratio1 * large_size1[1])
            final_height1 = large_size1[1]
        imaged1 = im1.resize((final_width1, final_height1), Image.ANTIALIAS)
        # imaged1.show()
        imaged1.save(self.Product_Img_1.path, quality=90)



        large_size2 = (1600, 1600)
        im2 = Image.open(self.Product_Img_2.path)
        image_w2, image_h2 = im2.size
        aspect_ratio2 = image_w2 / float(image_h2)
        new_height2 = int(large_size2[0] / aspect_ratio2)
        if new_height2 < 1600:
            final_width2 = large_size2[0]
            final_height2 = new_height2
        else:
            final_width2 = int(aspect_ratio2 * large_size2[1])
            final_height2 = large_size2[1]
        imaged2 = im2.resize((final_width2, final_height2), Image.ANTIALIAS)
        # imaged2.show()
        imaged2.save(self.Product_Img_2.path, quality=90)



        large_size3 = (1600, 1600)
        im3 = Image.open(self.Product_Img_3.path)
        image_w3, image_h3 = im3.size
        aspect_ratio3 = image_w3 / float(image_h3)
        new_height3 = int(large_size3[0] / aspect_ratio3)
        if new_height3 < 1600:
            final_width3 = large_size3[0]
            final_height3 = new_height3
        else:
            final_width3 = int(aspect_ratio3 * large_size3[1])
            final_height3 = large_size3[1]
        imaged3 = im3.resize((final_width3, final_height3), Image.ANTIALIAS)
        # imaged3.show()
        imaged3.save(self.Product_Img_3.path, quality=90)


        large_size4 = (1600, 1600)
        im4 = Image.open(self.Product_Img_4.path)
        image_w4, image_h4 = im4.size
        aspect_ratio4 = image_w4 / float(image_h4)
        new_height4 = int(large_size4[0] / aspect_ratio4)
        if new_height4 < 1600:
            final_width4 = large_size4[0]
            final_height4 = new_height4
        else:
            final_width4 = int(aspect_ratio4 * large_size4[1])
            final_height4 = large_size4[1]
        imaged4 = im4.resize((final_width4, final_height4), Image.ANTIALIAS)
        # imaged4.show()
        imaged4.save(self.Product_Img_4.path, quality=90)

        
        
        
        large_size5 = (1600, 1600)
        im5 = Image.open(self.Product_Img_5.path)
        image_w5, image_h5 = im5.size
        aspect_ratio5 = image_w5 / float(image_h5)
        new_height5 = int(large_size5[0] / aspect_ratio5)
        if new_height5 < 1600:
            final_width5 = large_size5[0]
            final_height5 = new_height5
        else:
            final_width5 = int(aspect_ratio5 * large_size5[1])
            final_height5 = large_size5[1]
        imaged5 = im5.resize((final_width5, final_height5), Image.ANTIALIAS)
        # imaged5.show()
        imaged5.save(self.Product_Img_5.path, quality=90)


        # imgObj1 = Image.open(self.Product_Img_1.path)
        # if imgObj1.height > 1600 or imgObj1.width >1600:
        #     output_size = (1600,1600)
        #     imgObj1.thumbnail(output_size)
        #     imgObj1.save(self.Product_Img_1.path)


    def __str__(self):
        return self.Product_Title

#############################################################################

# size
class Product_SubInformation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    Product_Sub_Information = models.CharField(max_length=256,null=True)

    def __str__(self):
        return self.Product_Sub_Information

# available sizes
class Information(models.Model):
    product_subInformation = models.ForeignKey(Product_SubInformation,on_delete=models.CASCADE)
    options = models.CharField(max_length=256)

    def __str__(self):
        return self.options

class ProductTags(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Product_Tags = models.CharField(max_length= 500)

    def __str__(self):
        return self.Product_Tags

class ProductPolicy(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Product_Policy = models.CharField(max_length=1150)

    def __str__(self):
        return self.Product_Policy

class AvailablePolicies(models.Model):
    policy = models.CharField(max_length=1000)
    def __str__(self):
        return self.policy


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Review_DateTime = models.DateTimeField(default = datetime.now())
    Review_Star_Select = models.CharField(max_length=10, default = '1', choices=(('1','1'),('1.5','1.5'),('2','2'),('2.5','2.5'),('3','3'),('3.5','3.5'),('4','4'),('4.5','4.5'),('5','5'),))
    Review_Discription = models.CharField(max_length=3500)

    def __str__(self):
        return self.Review_Discription