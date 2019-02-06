from django.contrib import admin
from .models import Product, Category, Brand, Tag


class AdminMixin:
    exclude = ['slug']

@admin.register(Product)
class ProductAdmin(AdminMixin, admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'count', 'price')


@admin.register(Category)
class CategoryAdmin(AdminMixin, admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Brand)
class BrandAdmin(AdminMixin, admin.ModelAdmin):
    list_display = ('name',)


