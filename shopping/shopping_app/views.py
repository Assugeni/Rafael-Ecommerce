from django.shortcuts import render
from django.http import HttpResponse
from .models import CATEGORY_CHOICES,ProductInfo,DataUpload

def homePageView(request):
    return render(request,'site/index.html')

def DetailPageView(request):
    return render(request,'site/product-details.html')

def CategoryDetailPageView(request):
    category = request.GET.get('category','')
    if category:
        # DataUpload.objects.filter()
        return render(request,'site/category_detail.html')
    else:
        return HttpResponse('Category not found')

def Cart(request):
    return render(request,'site/shop-cart.html')

def checkout(request):
    return render(request,'site/checkout.html')