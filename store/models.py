from django.db import models
from django.contrib.auth.models import User
#from django.urls import reverse


# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)
	
	class Meta:
		verbose_name_plural = 'Category'
		
	#def get_absolute_url(self):
	#	return reverse('product:detail', args=[self.slug])
	
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
	year_publish = models.CharField(max_length=20,blank=True)
	isbn_no = models.CharField(max_length=50,blank=True)
	in_stock = models.BooleanField(default=True)
	in_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Meta:
    verbose_name_plural = 'Product'
    ordering = ('-created',)

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