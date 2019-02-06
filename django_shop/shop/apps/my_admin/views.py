from django.views.generic import DetailView
from shop.apps.order.models import OrderModel
from shop.apps.order.mixins import ExportToPDFMixin

class DetailOrder(DetailView):
    template_name = 'my_admin/order.html'
    model = OrderModel


class DetailOrderPDF(ExportToPDFMixin, DetailView):
    model = OrderModel
    pdf_template = 'order/pdf-templates/order-pdf.html'

    def get(self, req, *args, **kwargs):
        context = {'order': self.get_object()}
        return self.to_pdf(context)