from gc import get_objects

from django.shortcuts import render, get_object_or_404
from .models import Product


def home(reqiest):
    return render(reqiest, 'index.html')


def contacts(reqiest):
    return render(reqiest, 'contacts.html')


def product_list(reqiest):
    products = Product.objects.all()
    context = {'products': products}
    return render(reqiest, 'product.html', context)


def product_detail(reqiest, pk):
    product = get_object_or_404(Product, id=pk)
    context = {'product': product}
    return render(reqiest, 'product_detail.html', context)
