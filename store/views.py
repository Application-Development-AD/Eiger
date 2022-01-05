from django.shortcuts import get_object_or_404, render
from .models import Category, Product

# Create your views here.

def search(request):
    context = {}
    return render (request, 'store/search.html', context)

def cart(request):
     context = {}
     return render(request, 'store/cart.html', context)

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