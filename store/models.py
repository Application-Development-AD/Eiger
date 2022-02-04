import email
from django.contrib.auth.forms import UsernameField
from typing import Reversible
from django.db import models
from django import urls
from django.forms.fields import EmailField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
	username = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	email = models.EmailField(max_length = 254)
	password1 = models.CharField(max_length=20)
	password2 = models.CharField(max_length=20)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)
	
	class Meta:
		verbose_name_plural = 'category'
		
#	def get_absolute_url(self):
#		return reverse('product:detail', args=[self.slug])
	
	def __str__(self):
		return self.name


class Product(models.Model):

	category = models.ForeignKey(Category,related_name='product', on_delete=models.CASCADE)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255,default='admin')
	description = models.TextField(blank=True)
	image = models.ImageField(null=True, blank=True)
	slug = models.SlugField(max_length=255)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	in_stock = models.BooleanField(default=True)
	in_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	digital = models.BooleanField(default=False,null=True, blank=True)
	tags = models.ManyToManyField(Tag)

#	class Meta:
#		verbose_name_plural = 'Products'
#		ordering = ('-created',)

#	def get_absolute_url(self):
#		return reverse('product:detail', args=[self.slug])
	
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url=''
		return url
		
	def __str__(self):
		return self.title 



class Order(models.Model):
	STATUS = (
		('Pending', 'Pending'),
		('Out for Delivery', 'Out for Delivery'),
		('Delivered', 'Delivered'),
	)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)
	status = models.CharField(max_length=100, null=True, choices=STATUS)

	
	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

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
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address