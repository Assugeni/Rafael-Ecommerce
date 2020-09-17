from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductInfo

def homePageView(request):
    return render(request,'site/index.html')

def DetailPageView(request):
    return render(request,'site/product-details.html')

def CategoryDetailPageView(request):
    category = request.GET.get('category','')
    size_list = ['S','M','L','XL','XXL']
    if category:
        category_data = ProductInfo.objects.filter(category=category)
        return render(request,'site/category_detail.html',{'category_data':category_data,
                                                           'category':category,
                                                           'size_list':size_list
                                                           })
    else:
        return HttpResponse('Category not found')

def Cart(request):
    return render(request,'site/shop-cart.html')

def checkout(request):
    return render(request,'site/checkout.html')