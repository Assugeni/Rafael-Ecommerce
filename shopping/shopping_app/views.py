from django.shortcuts import render
from django.http import HttpResponse
from .models import CATEGORY_CHOICES

def homePageView(request):
    return render(request,'site/index.html')

def DetailPageView(request):
    return render(request,'site/product-details.html')

def CategoryDetailPageView(request):
    return render(request,'site/category_detail.html')

def Cart(request):
    return render(request,'site/shop-cart.html')

def checkout(request):
    return render(request,'site/checkout.html')