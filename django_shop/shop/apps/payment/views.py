from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
from django.utils.decorators import method_decorator

from shop.apps.order.mixins import ExportToPDFMixin



@method_decorator(csrf_exempt, name='dispatch')
class PaymentResult(TemplateView):
    template_name = None




