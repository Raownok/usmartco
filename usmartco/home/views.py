from django.shortcuts import render
from . import models
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    productList = models.product.objects.all()
     #search code
    product_Name = request.GET.get('product_Name')
    if product_Name != '' and product_Name != None:
        productList = productList.filter(product_Name__icontains = product_Name)
    return render(request,'index.html',{'productList':productList})

def shop(request):
    productList = models.product.objects.all()

    #search code
    product_Name = request.GET.get('product_Name')
    if product_Name != '' and product_Name != None:
        productList = productList.filter(product_Name__icontains = product_Name)

    #paginator code:
    paginator = Paginator(productList,6)
    page = request.GET.get('page')
    productList = paginator.get_page(page)
    #-#
    return render(request,'shop.html',{'productList':productList})

def viewProduct(request,pk):
    product = models.product.objects.get(id = pk)
    return render(request,'elements.html',{"product":product})