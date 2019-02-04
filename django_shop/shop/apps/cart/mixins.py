from .utils import CartObj


class CartMixin:
    cart_context = False
    event = None

    def dispatch(self, request, *args, **kwargs):
        self.cart = CartObj(request)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {'cart_obj': self.cart}
        if self.cart_context:
            context.update(super().get_context_data(**kwargs))
        return context

    def cart_dispatch(self, req, event, *args):
        if event == 'clear':
            self.cart.action(event)
        else:
            product_id = req.POST.get('id')
            self.cart.action(event, product_id)
            return {'count': self.cart.count,
                    'count_order' : self.cart.count_order(product_id)}
