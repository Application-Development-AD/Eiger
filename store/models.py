from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	

	def __str__(self):
		return self.name


class Product(models.Model):
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
	title = models.CharField(max_length=255, null = True)
	author = models.CharField(max_length=255,default='admin')
	description = models.TextField(blank=True)
	image = models.ImageField(null=True, blank=True)
	slug = models.SlugField(max_length=255)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	in_stock = models.BooleanField(default=True)
	in_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


#class Meta:
#    verbose_name_plural = 'Products'
#    ordering = ('-created',)

#def get_absolute_url(self):
#	return reverse('product:detail', args=[self.slug])

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
	status = models.CharField(max_length=100, null=True, choices=STATUS)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def shipping (self):
		shipping = False
		orderitems = self.orderitem_set.all()
		shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems],decimal_places=2)
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
