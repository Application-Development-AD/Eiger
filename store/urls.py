from django.urls import path
from . import views 

urlpatterns = [
    path('', views.search, name="search"),
    path('cart/', views.cart, name="cart"),
    path('login/', views.login, name="login"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
]
 