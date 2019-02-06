from django.views.generic import CreateView


from .models import PayRecord, OrderModel
from shop.apps.cart.mixins import CartMixin
from shop.apps.core.mixins import JsonResponseMixin
from .mixins import ExportToPDFMixin


class OrderView(JsonResponseMixin, ExportToPDFMixin, CartMixin, CreateView):
    cart_context = True
    model = OrderModel
    fields = ['first_name', 'last_name', 'email', 'country', 'city', 'address',  'postal_code']
    template_name = 'order/order_form.html'
    pdf_template = 'order/pdf-templates/order-pdf.html'


    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.set_items(self.cart)
        self.cart_dispatch(self.request, 'clear')
        return self.to_pdf({'order': self.object})


