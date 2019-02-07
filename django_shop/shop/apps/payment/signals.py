from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.conf import settings


from shop.apps.order.models import OrderModel
from shop.apps.core.tasks import sendler_email

from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received


@receiver(valid_ipn_received)
def done_paypal(sender, **kwargs):
    # if sender.payment_status == ST_PP_COMPLETED:
    order = get_object_or_404(OrderModel, id=sender.invoice)
    order.paid = True
    order.save(update_fields=['paid'])
    order.make_sales()

    client_email = order.email
    html = render_to_string('order/pdf-templates/order-pdf.html', {'order': order})
    sendler_email.delay('Заказ №%s оплачен' % order.id,
                        'Дорогой, %s, вы успешно сделали заказ. Номер вашего заказа %s' % (order.first_name, order.id),
                        settings.DEFAULT_FROM_EMAIL, [client_email], pdf_data=html)


