from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductInfo
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Order,OrderItem
from django.contrib import messages


def homePageView(request):
    return render(request,'site/index.html')

class ProductView(DetailView):
    model = ProductInfo
    template_name = "site/product-details.html"

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

@login_required
def add_to_cart(request, pk):
    """
    Took data from product page and add it to cart page
    :param request:
    :param pk:
    :return:
    """
    product_info = get_object_or_404(ProductInfo, pk=pk )
    print(product_info)

    order_item, created = OrderItem.objects.get_or_create(
        product_info = product_info,
        user = request.user,
        ordered = False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(product_info__pk=product_info.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Added quantity Item")
            return redirect("order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "Item added to your cart")
            return redirect("order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added to your cart")
        return redirect("order-summary")

