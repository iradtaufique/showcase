from django.db import models


class Product(models.Model):
    PRODUCT_CATEGORY = (
        ('category1', 'category1'), ('category2', 'category2'),
        ('category3', 'category3'), ('category4', 'category4'),
    )
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='productImage')
    product_usage = models.CharField(max_length=255)
    sample1 = models.ImageField(upload_to='productImage')
    sample2 = models.ImageField(upload_to='productImage')
    sample3 = models.ImageField(upload_to='productImage')
    category = models.CharField(max_length=50, choices=PRODUCT_CATEGORY, default='category1')
