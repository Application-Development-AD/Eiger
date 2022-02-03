from django import forms
from django.http import response
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from store.forms import CreateUserForm
import store
from django.shortcuts import render
from .models import *

# Create your views here.

def main(request):
    category = Category.objects.all()
    context = {'category':category}
    return render (request, 'store/home.html', context)

def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {'products':products, 'category':category}
    return render (request, 'store/home.html', context)

def search(request):
    context = {}
    return render (request, 'store/search.html', context)

def cart(request):
     if request.user.is_authenticated:
          account = request.username.account
          order, created = Order.objects.get_or_create(account=account, complete=False)
          items = order.orderitem_set.all()
     else:
          items = []
          order ={'get_cart_total':0, 'get_cart_items':0}

     context = {'items' :items, 'order' : order}
     return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
          customer = request.username.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          items = order.orderitem_set.all()
    else:
          items = []
          order ={'get_cart_total':0, 'get_cart_items':0}
    
    context = {'items' :items, 'order' : order}
    return render(request, 'store/checkout.html', context)

def search(request):
     context = {}
     return render(request, 'store/cart.html', context)

def registrationPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'store/registration.html', context)

def login(request):
    context = {}
    return render(request, 'store/login.html', context)

def forgotpassword(request):
    context = {}
    return render(request, 'store/forgotpassword.html', context)

def accountDetails(request):
    context = {}
    return render(request, 'store/accountDetails.html', context)

def settings(request):
    context = {}
    return render(request, 'store/settings.html', context)

def payments(request):
    context = {}
    return render(request, 'store/payments.html', context)

def categories(request):
    return{
        'categories': Category.objects.all()
    }
    #context = {}
    #return render(request, 'store/category.html',context)

#get all product - query
def all_products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/home.html', context)

#get individual product
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product':product})

#get category page
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category':category, 'products':products})
