from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Product


def homePage(request):
    category1 = Product.objects.filter(category='category1')
    category2 = Product.objects.filter(category='category2')
    category3 = Product.objects.filter(category='category3')
    category4 = Product.objects.filter(category='category4')
    category5 = Product.objects.filter(category='category5')

    # p = Paginator([category1, category2], 1)
    # page_number = request.GET.get('page')
    # try:
    #     page_obj = p.get_page(page_number)
    # except PageNotAnInteger:
    #     page_obj = p.page(1)
    # except EmptyPage:
    #     page_obj = p.page(p.num_pages)

    context = {
        'category1': category1,
        'category2': category2,
        'category3': category3,
        'category4': category4,
        'category5': category5,
        # 'page_obj': page_obj,
    }
    return render(request, 'index.html', context)


def productDetails(request, id):
    details = Product.objects.get(id=id)
    context = {
        'details': details
    }
    return render(request, 'products/productDetails.html', context)
