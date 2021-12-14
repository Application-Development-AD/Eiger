from django.urls import path
from . import views 

urlpatterns = [
    path('', views.product, name="product"),
    path('cart/', views.cart, name="cart"),
    path('product/', views.product, name="product"),
    
]
