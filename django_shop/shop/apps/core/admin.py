from django.contrib import admin
from .models import Product, Category, Brand, Tag

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand')