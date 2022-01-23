from django.shortcuts import render
from .models import *

# Create your views here.

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

