from django.db import models
from django.utils.translation import gettext as _

from shop.apps.core.model_mixins import BaseShopMixin
from shop.apps.core.models import Product



class OrderModel(BaseShopMixin):
    first_name = models.CharField(_('Имя заказчика'), max_length=64)
    last_name = models.CharField(_('Фамилия заказчика'), max_length=64)
    address = models.CharField(_('Адресс заказчика'), max_length=200)
    country = models.CharField(_('Страна'), max_length=200)
    city = models.CharField(_('Город заказчика'), max_length=100)
    postal_code = models.CharField(_('Почтовый код'), max_length=100)
    paid = models.BooleanField(_('Оплачено'), default=False)
    total_price = models.FloatField(_('Итоговая цена'), default=0)
    email = models.EmailField('Email', max_length=124)

    def set_items(self, cart):
        for product, count, exceed in cart.get_items():
            if not exceed:
                price = product.price * count
                OrderItem.objects.create(count=count, type_product=product, price=price, order=self, brand=product.brand)
                self.total_price += price
        self.save(update_fields=['total_price'])

    @property
    def get_orders(self):
        return self.objects.orderitem_set.all()

    class Meta:
        ordering = ['-data_create']
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')

    def get_absolute_url(self):
        return '/'

class OrderItem(BaseShopMixin):
    count = models.PositiveIntegerField(_('Кол-во единиц товара'), default=1)
    type_product = models.ForeignKey(Product, verbose_name=_('Тип товара'), on_delete=models.PROTECT)
    price = models.FloatField(_('Цена'))
    order = models.ForeignKey(OrderModel, verbose_name=_("Ссылка на заказ"), on_delete=models.CASCADE)
    brand = models.CharField(max_length=124)

    def __repr__(self):
        return str(self.id)


    class Meta:
        ordering = ['-price']
        verbose_name = _('Единица заказа')
        verbose_name_plural = _('Единицы заказа')



class PayRecord(BaseShopMixin):
    pass
