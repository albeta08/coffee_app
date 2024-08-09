from django.contrib import admin
from .models import Product

class ProductAdmnin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price', 'available','photo']
    search_fields = ['name']

admin.site.register(Product, ProductAdmnin)