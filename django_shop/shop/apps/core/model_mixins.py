from django.db import models
from django.utils import timezone







class BaseShopMixin(models.Model):

    data_create = models.DateTimeField(default=timezone.now)
    data_change = models.DateTimeField(default=timezone.now)


    class Meta:
        abstract = True



class ShopMixin(BaseShopMixin):

    stat = (('A', 'Active'),
            ('D', 'Deactive'))

    image = models.ImageField(upload_to='/media/shop_media')
    status = models.CharField(choices=stat, max_length=20)
    description = models.TextField()

    class Meta:
        abstract = True