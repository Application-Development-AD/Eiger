from django.shortcuts import render

# Create your views here.

def search(request):
    context = {}
    return render (request, 'store/search.html', context)

def cart(request):
     context = {}
     return render(request, 'store/cart.html', context)

def product(request):
     context = {}
     return render(request, 'store/product.html', context)