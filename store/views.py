from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.shortcuts import render
from .models import *
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.


@login_required(login_urls='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers,
    'total_orders':total_orders, 'delivered':delivered,
    'pending':pending}

    return render(request, 'accounts/dashboard.html',context)

def userPage(request):
    context={}
    return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/product.html', {'products':products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
    customer = Customer.objects.all(id=pk_test)

    orders = customer.order_set.all()
    order_count =orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer':customer, 'orders':orders, 'orders_count':order_count,
    'myFilter':myFilter}
    return render(request, 'accounts/customer.html', context)

@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')            
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            message.info(request, 'Username OR password is wrong')
            
        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


