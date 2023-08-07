from django.shortcuts import render
from product.models import *

def product(request):
    product_categories = Product_category.objects.all()
    if request.method == "GET":
        product_categories = product_categories
    elif request.method == "POST":
        
        product_cat = Product_category.objects.get(id=request.POST.get('product_category'))
        sub_categories = product_cat.sub_product_category1_set.all()
        
    return render(request, 'product.html', locals())


def product_reg(request):
    return render(request, 'product_reg.html')

