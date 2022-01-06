from django.contrib.auth.forms import UsernameField
from typing import Reversible
from django.db import models
from django import urls
from django.forms.fields import EmailField
from django.contrib.auth.models import User
from django.urls import reverse

class Account(models.Model):
	username = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	email = models.CharField(max_length=200)
	password2 = models.CharField(max_length=20)
	name = models.CharField(max_length=200, null=True)
	password = models.CharField(max_length=20)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)
	
	class Meta:
		verbose_name_plural = 'categories'
		
	def get_absolute_url(self):
		return reverse('product:product_detail', args=[self.slug])
	
	def __str__(self):
		return self.name


class Product(models.Model):
	category = models.ForeignKey(Category,related_name='product', on_delete=models.CASCADE)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255,default='admin')
	description = models.TextField(blank=True)
	image = models.ImageField(null=True, blank=True, upload_to='images/')
	slug = models.SlugField(max_length=255)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	in_stock = models.BooleanField(default=True)
	in_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Meta:
    verbose_name_plural = 'Products'
    ordering = ('-created',)

def get_absolute_url(self):
	return reverse('product:product_detail', args=[self.slug])
   

@property
def imageURL(self):
	try:
		url = self.image.models.url
	except: 
		url =''
	return url
	
def __str__(self):
    return self.title 



class Order(models.Model):
	customer = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

	

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
