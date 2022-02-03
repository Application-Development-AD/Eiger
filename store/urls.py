from django.urls import path
from . import views 

app_name = 'store'

urlpatterns = [
    path('', views.home, name="home"),
    path('', views.search, name="search"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('registration/', views.register_request, name="registration"),
    path('login/', views.login, name="login"),
    path('', views.logout, name="logout"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('accountDetails/', views.accountDetails, name="accountDetails"),
    path('settings/', views.settings, name="settings"),
    path('payments/', views.payments, name="payments"),
    path('', views.all_products, name='all_products'),
    path('book/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]
 