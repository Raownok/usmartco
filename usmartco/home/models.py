from django.db import models

# Create your models here.
class product(models.Model):
    product_Name  = models.CharField(max_length=200)
    product_Details = models.TextField(blank=True,null=True)
    product_Price = models.CharField(max_length=50)
    product_Image = models.ImageField(upload_to='product_Images',blank=True,null=True)