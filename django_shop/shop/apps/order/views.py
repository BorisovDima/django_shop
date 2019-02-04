from django.views.generic import CreateView
from .models import PayRecord, OrderModel
from shop.apps.cart.mixins import CartMixin
from shop.apps.core.mixins import JsonResponseMixin

class OrderView(JsonResponseMixin, CartMixin, CreateView):
    cart_context = True
    model = OrderModel
    fields = ['first_name', 'last_name', 'address', 'city', 'postal_code']
    template_name = 'order/order_form.html'


    def form_valid(self, form):
        r = super().form_valid(form)
        self.object.set_items(self.cart)
        self.cart_dispatch(self.request, 'clear')
        return r
