from django.http import response
from django.shortcuts import render

import store

# Create your views here.

def search(request):
    context = {}
    return render (request, 'store/search.html', context)

def cart(request):
     context = {}
     return render(request, 'store/cart.html', context)

# Start 
def registration(request):
    context = {}
    return render(request, 'store/registration.html', context)
# End