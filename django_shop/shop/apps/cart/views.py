from django.views.generic import ListView


from .mixins import CartMixin
from shop.apps.core.mixins import JsonResponseMixin



class CartView(JsonResponseMixin, CartMixin, ListView):

    def get(self, req, *args, **kwargs):
        return self.get_context_data()


    def post(self, req, *args, **kwargs):
        return self.cart_dispatch(req, self.event)


