
from django.shortcuts import render
from .models import *
#from .models import Category, Product

# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

def category(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'store/category.html', context)

