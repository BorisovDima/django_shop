from django.views.generic import CreateView, DetailView, View
from django.conf import settings
from django.shortcuts import get_object_or_404

from .models import OrderModel
from shop.apps.cart.mixins import CartMixin




class OrderView(CartMixin, CreateView):
    cart_context = True
    model = OrderModel
    fields = ['first_name', 'last_name', 'email', 'country', 'city', 'address',  'postal_code']
    template_name = 'order/order_form.html'


    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.set_items(self.cart)
        self.cart_dispatch(self.request, 'clear')
        self.request.session[settings.ORDER_SESSION_ID] = self.object.id
        return response


class OrderPaymentPageView(DetailView):
    template_name = 'order/order_payment.html'

    def get_object(self, queryset=None):
        return get_object_or_404(OrderModel, **{'id': self.request.session.get(settings.ORDER_SESSION_ID),
                                                'paid': False})









