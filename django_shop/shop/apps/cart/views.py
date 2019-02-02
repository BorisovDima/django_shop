from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from shop.apps.core.serializers import ProductSerializer
from .mixins import CartMixin
from shop.apps.core.models import Product
from shop.apps.core.mixins import ListRestMixin

class CartView(CartMixin, ListRestMixin, ModelViewSet):
    event = None
    serializer_class = ProductSerializer
    list_key = 'products'

    def get_queryset(self):
        keys = self.cart.get_keys()
        return Product.objects.filter(id__in=keys)

    @action(detail=False, methods=['post'])
    def put_order(self, req, *args, **kwargs):
        product_id = req.POST.get('id')
        self.cart.action(self.event, product_id)
        return Response({'count': self.cart.count})




