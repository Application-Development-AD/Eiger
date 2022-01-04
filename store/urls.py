from django.urls import path
from . import views 

urlpatterns = [
    path('main/', views.main, name="main"),
    path('', views.search, name="search"),
    path('cart/', views.cart, name="cart"),
<<<<<<< HEAD
    path('registration/', views.registration_view, name="registration"),
=======
    path('login/', views.login, name="login"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('accountDetails/', views.accountDetails, name="accountDetails"),
    path('settings/', views.settings, name="settings"),
    path('payments/', views.payments, name="payments"),
>>>>>>> main
]
 