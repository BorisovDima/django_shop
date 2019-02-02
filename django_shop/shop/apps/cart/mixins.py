from .utils import CartObj

class CartMixin:
    def dispatch(self, request, *args, **kwargs):
        self.cart = CartObj(request)
        return super().dispatch(request, *args, **kwargs)


