from .utils import CartObj
from shop.apps.core.models import Variant

class CartMixin:
    cart_context = False
    event = None
    product_model = Variant

    def dispatch(self, request, *args, **kwargs):
        self.cart = CartObj(request)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {'cart_obj': self.cart}
        if self.cart_context:
            context.update(super().get_context_data(**kwargs))
        return context

    def cart_dispatch(self, req, event, *args):
        product_id = req.POST.get('id')
        self.cart.action(event, product_id)
        kwargs = {'count': self.cart.count}
        if event in ['add', 'delete']:
            count = self.cart.orders.get(product_id)
            p = self.product_model.objects.get(id=product_id)
            kwargs.update({'count_order': self.cart.count_order(product_id), 'extra': [p.count < count, p.count],
                           'price': p.price * count})
        return kwargs
