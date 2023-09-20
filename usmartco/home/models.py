from django.db import models

# Create your models here.
class product(models.Model):
    product_Name  = models.CharField(max_length=200)
    product_Type = models.CharField(max_length=200, blank=True, null=True)
    product_Condition = models.CharField(max_length=200, blank=True, null=True)
    product_Details = models.TextField(blank=True,null=True)
    product_Price = models.CharField(max_length=50)
    product_Image1 = models.ImageField(upload_to='product_Images',blank=True,null=True)
    product_Image2 = models.ImageField(upload_to='product_Images',blank=True,null=True)
    product_Image3 = models.ImageField(upload_to='product_Images',blank=True,null=True)
    product_Image4 = models.ImageField(upload_to='product_Images',blank=True,null=True)
    product_Image5 = models.ImageField(upload_to='product_Images',blank=True,null=True)
    product_Image6 = models.ImageField(upload_to='product_Images',blank=True,null=True)

class featuedProduct(models.Model):
    product_Name  = models.CharField(max_length=200)
    product_Type = models.CharField(max_length=200, blank=True, null=True)
    product_Condition = models.CharField(max_length=200, blank=True, null=True)
    product_Details = models.TextField(blank=True,null=True)
    product_Price = models.CharField(max_length=50)
    product_Image1 = models.ImageField(upload_to='product_Images',blank=True,null=True)
    product_Image2 = models.ImageField(upload_to='product_Images',blank=True,null=True)
    product_Image3 = models.ImageField(upload_to='product_Images',blank=True,null=True)
    product_Image4 = models.ImageField(upload_to='product_Images',blank=True,null=True)
    product_Image5 = models.ImageField(upload_to='product_Images',blank=True,null=True)
    product_Image6 = models.ImageField(upload_to='product_Images',blank=True,null=True)