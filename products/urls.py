from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name='homepage'),
    path('product-details/<int:id>', productDetails, name='product_details'),
]