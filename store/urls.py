from django.urls import path
from . import views 

urlpatterns = [
  #  path('', views.home, name="home"),
  #  path('main/', views.main, name="main"),
  #  path('', views.search, name="search"),
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    
    path('update_item/', views.updateItem, name="update_item"),
    path('process-order/', views.processOrder, name="process-order"),
  #  path('registration/', views.registration_view, name="registration"),
  #  path('login/', views.login, name="login"),
  # path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
  #  path('accountDetails/', views.accountDetails, name="accountDetails"),
  #  path('settings/', views.settings, name="settings"),
  #  path('payments/', views.payments, name="payments"),
  #  path('', views.all_products, name='all_products'),
  #  path('book/<slug:slug>/', views.product_detail, name='product_detail'),
  #  path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]
