from django.views.generic import ListView
from django.template.loader import render_to_string

from .mixins import CartMixin
from shop.apps.core.mixins import JsonResponseMixin



class CartView(JsonResponseMixin, CartMixin, ListView):

    def get(self, req, *args, **kwargs):
        return {'html': render_to_string(self.template_name, self.get_context_data())}


    def post(self, req, *args, **kwargs):
        return self.cart_dispatch(req, self.event)


