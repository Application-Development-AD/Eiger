from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {'products':products, 'category':category}
    return render (request, 'store/home.html', context)


def cart(request):
     if request.user.is_authenticated:
          customer = request.username.customer
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

