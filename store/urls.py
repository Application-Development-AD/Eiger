from django.urls import path
from . import views 

app_name = 'store'

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name="home"),
=======
    path('home/', views.home, name="home"),
>>>>>>> 556e7108152af0c97d6043c39925b984d2b71f19
  #  path('', views.search, name="search"),
    path('cart/', views.cart, name="cart"),
    path('registration/', views.registration_view, name="registration"),
    path('login/', views.login, name="login"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('accountDetails/', views.accountDetails, name="accountDetails"),
    path('settings/', views.settings, name="settings"),
    path('payments/', views.payments, name="payments"),
    path('', views.all_products, name='all_products'),
    path('book/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]
 