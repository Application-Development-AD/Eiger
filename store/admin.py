from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)


#@admin.register(Category)
#class CategoryAdmin(admin.ModelAdmin):
#    list_display = ['name', 'slug']
 #   prepopulated_fields = {'slug':('name',)}

#@admin.register(Product)
#class ProductAdmin(admin.ModelAdmin):
 #   list_display = ['title','author','slug','price',
 #                'in_stock','created','updated']
 #   list_filter = ['in_stock','in_active']
 #   prepopulated_fields = {'slug':('title',)}