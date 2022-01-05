from django.shortcuts import render
from .models import Category, Product

# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products':products})

def search(request):
    context = {}
    return render (request, 'store/search.html', context)

def cart(request):
     context = {}
     return render(request, 'store/cart.html', context)

def category(request):
    context = {}
    return render(request, 'store/category.html',context)