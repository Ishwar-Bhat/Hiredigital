from django.contrib.auth.models import User
from django.db import models


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.category_name


class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50, null=False)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING)
    product_image = models.CharField(max_length=255, null=True)
    product_stock = models.IntegerField(null=False, default=0)
    product_price = models.FloatField(null=False)
    selling_price = models.FloatField(null=False)
    created_date = models.DateField(auto_now=True, null=False)
    updated_date = models.DateField(auto_now=True, null=False)
    created_by = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('updated_date', 'product_id')
