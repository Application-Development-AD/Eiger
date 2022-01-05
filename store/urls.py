from django.urls import path
from . import views 

app_name = 'store'

urlpatterns = [
    path('', views.search, name="search"),
    path('cart/', views.cart, name="cart"),
    path('', views.all_products, name='all_products'),
]
