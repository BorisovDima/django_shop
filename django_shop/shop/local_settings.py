

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_shop',
        'USER': 'root',
        'PASSWORD': '1488',
    }
}


CART_SESSION_KEY = 'orders_'
MAX_CART_SIZE = 10

PAYPAL_RECEIVER_EMAIL = 'dmitriy_shvidkiy@mail.ru'
PAYPAL_TEST = True