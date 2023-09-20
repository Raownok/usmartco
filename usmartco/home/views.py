from django.shortcuts import render
from . import models
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    productList = models.product.objects.all()
    featuredProductList = models.featuedProduct.objects.all()
    list = {
        'productList':productList,
        'featuredProductList':featuredProductList,
    }
    
    return render(request,'index.html',list)

def about(request):
    return render(request, 'about.html')

def shop(request):
    productList = models.product.objects.all()

    # #search code
    # product_Name = request.GET.get('product_Name')
    # if product_Name != '' and product_Name != None:
    #     productList = productList.filter(product_Name__icontains = product_Name)

    #paginator code:
    paginator = Paginator(productList,6)
    page = request.GET.get('page')
    productList = paginator.get_page(page)
    #-#
    return render(request,'shop.html',{'productList':productList})

def viewProduct(request,pk):
    productList = models.product.objects.all()
    
    # #search code
    # product_Name = request.GET.get('product_Name')
    # if product_Name != '' and product_Name != None:
    #     productList = productList.filter(product_Name__icontains = product_Name)
    
    product = models.product.objects.get(id = pk)

    
    return render(request,'elements.html',{'product' : product})

def viewFeaturedProduct(request,pk):
    
    
    # #search code
    # product_Name = request.GET.get('product_Name')
    # if product_Name != '' and product_Name != None:
    #     productList = productList.filter(product_Name__icontains = product_Name)
    
    product = models.featuedProduct.objects.get(id = pk)

    
    return render(request,'elements.html',{'product' : product})


def searchResult(request):
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
    return render(request,'search.html',{'productList':productList})

def skinCare(request):
    productList = models.product.objects.all()

    # #search code
    # product_Name = request.GET.get('product_Name')
    # if product_Name != '' and product_Name != None:
    #     productList = productList.filter(product_Name__icontains = product_Name)

    # #paginator code:
    # paginator = Paginator(productList,6)
    # page = request.GET.get('page')
    # productList = paginator.get_page(page)
    # #-#
    return render(request,'skinCare.html',{'productList':productList})
def hairCare(request):
    productList = models.product.objects.all()

    # #search code
    # product_Name = request.GET.get('product_Name')
    # if product_Name != '' and product_Name != None:
    #     productList = productList.filter(product_Name__icontains = product_Name)

    # #paginator code:
    # paginator = Paginator(productList,6)
    # page = request.GET.get('page')
    # productList = paginator.get_page(page)
    # #-#
    return render(request,'hairCare.html',{'productList':productList})
def makeup(request):
    productList = models.product.objects.all()

    # #search code
    # product_Name = request.GET.get('product_Name')
    # if product_Name != '' and product_Name != None:
    #     productList = productList.filter(product_Name__icontains = product_Name)

    # #paginator code:
    # paginator = Paginator(productList,6)
    # page = request.GET.get('page')
    # productList = paginator.get_page(page)
    # #-#
    return render(request,'makeup.html',{'productList':productList})
def perfume(request):
    productList = models.product.objects.all()

    # #search code
    # product_Name = request.GET.get('product_Name')
    # if product_Name != '' and product_Name != None:
    #     productList = productList.filter(product_Name__icontains = product_Name)

    # #paginator code:
    # paginator = Paginator(productList,6)
    # page = request.GET.get('page')
    # productList = paginator.get_page(page)
    # #-#
    return render(request,'perfumes.html',{'productList':productList})