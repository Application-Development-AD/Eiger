from django.urls import path
from . import views 

app_name = 'store'

urlpatterns = [
    path('', views.home, name="home"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

    path('', views.search, name="search"),
    path('registration/', views.registrationPage, name="registration"),
    path('login/', views.login, name="login"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('accountDetails/', views.accountDetails, name="accountDetails"),
    path('book/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
 
]
 