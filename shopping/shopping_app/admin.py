from django.contrib import admin
from .models import ProductInfo,DataUpload

# Register your models here.
admin.site.register(ProductInfo)
admin.site.register(DataUpload)