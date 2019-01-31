from django.db import models
from .model_mixins import BaseShopMixin, ShopMixin



class Tag(BaseShopMixin):
    pass


class Brand(ShopMixin):
    pass

class Category(ShopMixin):
    pass

class Product(ShopMixin):
    pass



