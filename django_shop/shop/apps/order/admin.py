from django.contrib import admin
from .models import OrderModel, OrderItem



class OrderInline(admin.TabularInline):
    model = OrderItem


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'address', 'city', 'total_price', 'paid')
    inlines = [OrderInline]


admin.site.register(OrderItem)
