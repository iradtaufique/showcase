from django.shortcuts import render
from .models import Product


def homePage(request):
    datas = Product.objects.filter(category='category1')
    context = {'datas': datas}
    return render(request, 'index.html', context)


def productDetails(request, id):
    details = Product.objects.get(id=id)
    context = {
        'details': details
    }
    return render(request, 'products/productDetails.html', context)
