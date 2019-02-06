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

    CHOISE_SIZE= (('S','S'),
                  ('M','M'),
                  ('L','L'),
                  ('XL','XL'),
                  ('2XL','2XL'),
                  ('3XL','3XL'),
                  ('4XL','4XL'),
                  ('5XL','5XL'))

    features = models.CharField(max_length=524, null=True, blank=True)
    public_name = models.CharField(max_length=124, null=True, blank=True)
    size = models.CharField(_('Размер товара'), max_length=15, choices=CHOISE_SIZE, null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name=_('Категория товара'), on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name=_('Бренд товара'), on_delete=models.CASCADE)
    price = models.FloatField(_('Цена товара'))
    count = models.IntegerField(_('Кол-во единиц товара'), default=1)
    sales = models.PositiveIntegerField(_('Кол-во проданных единиц товара'), default=0)

    def save(self, *args, **kwargs):
        if self.size:
            self.public_name = self.name
            self.name = '%s-%s' % (self.name, self.size)
        super().save(*args, **kwargs)

    @property
    def get_name(self):
        return self.public_name if self.public_name else self.name

    class Meta:
        ordering = ['-sales']
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

