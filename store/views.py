import re
from django import forms
from django.http import response
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import store
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.sessions.models import Session
# Create your views here.
from store.forms import CreateUserForm
from django.http import JsonResponse
import json
import datetime
from . models import * 
from . utils import *

def main(request):
    category = Category.objects.all()
    context = {'category':category}
    return render (request, 'store/home.html', context)

def search(request):
    context = {}
    #return render(request, 'store/cart.html', context)

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

def home(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/home.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

def register_request(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        Customer(username=username, email=email, password1=password1, password2=password2).save(),
        return render(request, 'store/registration.html')

    else :
        return render(request, 'store/registration.html')


def login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            userdetails = Customer.objects.get(username = username, password1 = password)
            print("username", userdetails)
            request.session['username'] = userdetails.username

            customer = Customer.objects.filter(username = username)
            if  request.session['username'] == 'admin':
                if  password == 'admin123':
                    return render(request, 'store/dashboard.html', {'customer' : customer})
            else:
                return render(request, 'store/home.html', {'customer' : customer})
        except Customer.DoesNotExist as e:
            messages.success(request, 'Username/Password Invalid!')
    context = {}
    return render(request, 'store/login.html', context)

def logout(request):
    try:
        del request.session['username']
    except:
        return render(request, 'store/home.html')
    return render(request, 'store/home.html')

def forgotpassword(request):
    context = {}
    return render(request, 'store/forgotpassword.html', context)