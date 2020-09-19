from django.contrib import admin
from .models import ProductInfo,DataUpload,OrderItem,Payment,CheckoutAddress

# Register your models here.
admin.site.register(ProductInfo)
admin.site.register(DataUpload)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(CheckoutAddress)
