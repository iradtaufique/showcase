from django.db import models


class Product(models.Model):
    PRODUCT_CATEGORY = (
        ('category1', 'category1'), ('category2', 'category2'),
        ('category3', 'category3'), ('category4', 'category4'),
        ('category5', 'category5'),
    )
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=50, choices=PRODUCT_CATEGORY, default='category1')

    def __str__(self):
        return self.product_name


""" class for storing product image"""
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='ProductImage')
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
