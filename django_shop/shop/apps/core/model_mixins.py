from django.db import models
from django.utils import timezone

from .utils import my_slugify





class BaseShopMixin(models.Model):

    data_create = models.DateTimeField(default=timezone.now)
    data_update = models.DateTimeField(default=timezone.now)


    class Meta:
        abstract = True



class ShopMixin(BaseShopMixin):

    stat = (('A', 'Active'),
            ('D', 'Deactive'))

    image = models.ImageField(upload_to='shop_media/')
    status = models.CharField(choices=stat, max_length=20, default='A')
    description = models.TextField()
    slug = models.SlugField(allow_unicode=True, max_length=65)
    name = models.CharField(max_length=124)


    def save(self, *args, **kwargs):
        self.slug = my_slugify(self.name)
        super().save()

    class Meta:
        abstract = True


