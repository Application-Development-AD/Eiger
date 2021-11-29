from django.shortcuts import render

# Create your views here.

def search(request):
    context = {}
    return render (request, 'store/search.html', context)
