from django.urls import path
from . import views 

urlpatterns = [
<<<<<<< HEAD
    path('main/', views.main, name="main"),
    path('', views.search, name="search"),
    path('cart/', views.cart, name="cart"),
    path('login/', views.login, name="login"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('accountDetails/', views.accountDetails, name="accountDetails"),
    path('settings/', views.settings, name="settings"),
    path('payments/', views.payments, name="payments"),
=======
    path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('search/', views.checkout, name="search"), 
>>>>>>> main
]
 