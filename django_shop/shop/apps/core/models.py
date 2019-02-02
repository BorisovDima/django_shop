from django.db import models
from django.utils.translation import gettext as _

from .model_mixins import BaseShopMixin, ShopMixin


class Tag(BaseShopMixin):
    pass


class Brand(ShopMixin):
    class Meta:
        verbose_name = _('Бренд')
        verbose_name_plural = _('Бренд')

class Category(ShopMixin):
    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

class Product(ShopMixin):
    category = models.ForeignKey(Category, verbose_name=_('Категория товара'), on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name=_('Бренд товара'), on_delete=models.CASCADE)
    price = models.FloatField(_('Цена товара'))
    count = models.IntegerField(_('Кол-во единиц товара'), default=1)
    sales = models.PositiveIntegerField(_('Кол-во проданных единиц товара'), default=0)

    class Meta(ShopMixin.Meta):
        ordering = ['-sales']
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

