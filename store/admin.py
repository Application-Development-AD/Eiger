from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Account)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
#admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','author','slug','price',
                 'in_stock','created','updated']
    list_filter = ['in_stock','in_active']
<<<<<<< HEAD
    prepopulated_fields = {'slug':('title',)}


=======
    list_editable = ['price','in_stock']
    prepopulated_fields = {'slug':('title',)}
>>>>>>> eiger_nasrin
