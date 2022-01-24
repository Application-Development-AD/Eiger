from django.shortcuts import render
from .models import *

# Create your views here.

def main(request):
    context = {}
    return render (request, 'store/main.html', context)

def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render (request, 'store/home.html', context)

def search(request):
    context = {}
    return render (request, 'store/search.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

