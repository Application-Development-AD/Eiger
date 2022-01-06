from django import forms
from django.http import response
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from store.forms import RegistrationForm
import store
from django.shortcuts import render
from .models import *
from .models import Category, Product

# Create your views here.

def main(request):
    context = {}
    return render (request, 'store/main.html', context)

def search(request):
    context = {}
    return render (request, 'store/search.html', context)

def cart(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          items = order.orderitem_set.all()
     else:
          items = []
          order ={'get_cart_total':0, 'get_cart_items':0}

     context = {'items' :items, 'order' : order}
     return render(request, 'store/cart.html', context)

def checkout(request):
      context = {}
      return render(request, 'store/checkout.html', context)

def search(request):
     context = {}
     return render(request, 'store/cart.html', context)

# Start 
def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('raw_password')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'store/registration.html', {'form': form})
    # return render(request, 'store/registration.html', context)
# End

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

#get all product
def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products':products})

#get individual product
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product':product})

#get category page
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category':category, 'products':products})
