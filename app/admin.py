from django.contrib import admin
from . models import Products
@admin.register(Products)
# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']
