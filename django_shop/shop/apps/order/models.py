from django.db import models
from shop.apps.core.model_mixins import BaseShopMixin

class Order(BaseShopMixin):
    pass


class PayRecord(BaseShopMixin):
    pass
