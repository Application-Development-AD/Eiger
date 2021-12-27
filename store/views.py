from django.shortcuts import render

# Create your views here.

def search(request):
    context = {}
    return render (request, 'store/search.html', context)

def cart(request):
     context = {}
     return render(request, 'store/cart.html', context)

def login(request):
    context = {}
    return render(request, 'store/login.html', context)

def forgotpassword(request):
    context = {}
    return render(request, 'store/forgotpassword.html', context)

def accountDetails(request):
    context = {}
    return render(request, 'store/accountDetails.html', context)