from django.conf import settings
from shop.apps.core.models import Product


CART_SESSION_KEY = settings.CART_SESSION_KEY
MAX_CART_SIZE = settings.MAX_CART_SIZE

class CartObj:
    def __init__(self, request):
        self.session = request.session
        self.orders = request.session.setdefault(CART_SESSION_KEY, {})
        self.items = None


    def get_items(self):
        if not self.items:
            pk = [key for key,_ in self]
            self.items = Product.objects.filter(id__in=pk)
        for p in self.items:
            yield p, self.orders[str(p.id)], self.exceed(p)

    def __iter__(self):
       yield from self.orders.items()

    def action(self, event, *args):
        self.session.modified = True
        return getattr(self, event)(*args)


    def add(self, id):
        if self.orders.get(id):
            self.orders[id] += self.orders[id] < MAX_CART_SIZE
        else:
            self.orders[id] = 1
        return self.exceed(Product.objects.get(id=id))


    def delete(self, id):
        self.orders[id] -= self.orders[id] > 1

    def delete_all(self, id):
        del self.orders[id]

    def clear(self):
        self.orders.clear()

    def exceed(self, prod):
        return prod.count < self.orders[str(prod.id)]


    def count_order(self, id):
        return self.orders.get(id)

    @property
    def count(self):
        return sum((val for _, val in self))


    @property
    def total_price(self):
        return sum((float(obj.price)*count for obj, count, exceed in self.get_items() if not exceed))