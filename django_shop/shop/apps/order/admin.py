from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.conf import settings


from .models import OrderModel, OrderItem, Shipping
from .mixins import ExportToCSVMixin




class OrderInline(admin.TabularInline):
    model = OrderItem
    exclude = ('data_update',)
    extra = 0

@admin.register(OrderModel)
class OrderAdmin(ExportToCSVMixin, admin.ModelAdmin):
    list_display = ('last_name', 'address', 'city', 'total_price', 'paid', 'DateCreate', 'OrderDetail', 'OrderDetailPDF')
    inlines = [OrderInline]
    actions = ['to_csv']
    csv_filename = 'orders.csv'

    def DateCreate(self, order):
        return order.date_create.strftime(settings.ADMIN_DATE_FORMAT)
    DateCreate.short_description = 'Дата создания'

    def OrderDetailPDF(self, order):
        return format_html('<a href=%s>PDF</a>' % reverse('my-admin:detail-order-pdf', kwargs={'pk': order.id}))
    OrderDetailPDF.short_description = 'PDF'

    def OrderDetail(self, order):
        return format_html('<a href=%s>Подробнее</a>' % reverse('my-admin:detail-order', kwargs={'pk': order.id}))
    OrderDetail.short_description = 'Подробнее'


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ('id', 'price', 'date_create')
    search_fields = ('=id',)


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    pass




