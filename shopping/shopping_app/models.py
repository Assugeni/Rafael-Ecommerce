from django.db import models
from django.utils import timezone
import os
# Create your models here.
CATEGORY_CHOICES = (
    ("Women", "Women"),
    ("Men", "Men"),
    ("Kids", "Kids"),
    ("Accessories", "Accessories"),
    ("Cosmetics", "Cosmetics"),
)

ADMIN_CHOICES = (
    ("admin","admin"),
)
# declaring a Category Model
class ProductInfo(models.Model):
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='1'
    )
    product_title = models.CharField(max_length=100)
    uploaded_by = models.CharField(
        max_length=20,
        choices=ADMIN_CHOICES,
        default='Women'
    )
    uploaded_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.product_title + ",Category : "+self.category

class DataUpload(models.Model):
    product_info = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    image = models.ImageField()

    def save(self):
        for field in self._meta.fields:
            if field.name == 'image':
                field.upload_to = self.product_info.category+'/'+self.product_info.product_title
        super(DataUpload, self).save()

    def __str__(self):
        return str(self.product_info.product_title)+" - "+str(self.id)
