from django.contrib import admin
from . import models
# Register your models here.
class product_Admin(admin.ModelAdmin):
    list_display = [
        "product_Name",
        "product_Price",
    ]
    search_fields = ('product_Name',)

class featuredProduct_Admin(admin.ModelAdmin):
    list_display = [
        "product_Name",
        "product_Price",
    ]
    search_fields = ('product_Name',)

admin.site.site_header = "usmartco."
admin.site.site_title = "usmartco Admin-Panel"
admin.site.index_title = "Manage usmartco."

admin.site.register(models.product,product_Admin)
admin.site.register(models.featuedProduct,featuredProduct_Admin)