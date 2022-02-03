from django.urls import path
from . import views 

app_name = 'store'

urlpatterns = [
   path('', views.store, name='store'),
   path('checkout/',views.checkout, name='checkout')
   path('user/', views.userPage, name='user-page')
]
