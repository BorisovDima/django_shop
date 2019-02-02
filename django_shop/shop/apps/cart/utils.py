import json

FORMAT_CART_SESSION = 'order_'


class CartObj:
    def __init__(self, request):
        self.format = FORMAT_CART_SESSION + '%s'
        self.session = request.session

    def __iter__(self):
       for key, v in self.session.items():
           if key.startswith(FORMAT_CART_SESSION):
                yield v

    def action(self, event, id):
        self.add(id) if event == 'add' else self.delete(id)
        self.session.modified = True

    def add(self, id):
        if not self.session.get(self.format % id):
            self.session[self.format % id] = {'id': id, 'count': 1}
        else:
            self.session[self.format % id]['count'] += 1

    def delete(self, id):
        self.session[self.format % id]['count'] -= 1

    def get_keys(self):
        return [key['id'] for key in self]

    @property
    def count(self):
        return sum((int(val['count']) for val in self))