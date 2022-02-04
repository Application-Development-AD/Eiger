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
    
    path('book/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),

    path('user/', views.userPage, name="user-page"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    
    path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
 
]
 