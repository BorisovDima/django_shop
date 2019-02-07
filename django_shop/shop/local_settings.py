

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_shop',
        'USER': 'root',
        'PASSWORD': '1488',
    }
}


STATIC_ROOT = '/var/www/shopdjango.ru/static'


CART_SESSION_KEY = 'orders_'
ORDER_SESSION_ID = 'order_id'

MAX_CART_SIZE = 10

PAYPAL_RECEIVER_EMAIL = 'dmitriy_shvidkiy@mail.ru'
PAYPAL_TEST = True


SESSION_COOKIE_AGE =  1209600 * 2



######## Celery ####################

REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'

########### mail #######

DEFAULT_FROM_EMAIL = 'dmitriy_shvidkiy@mail.ru'
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = 'dmitriy_shvidkiy@mail.ru'
EMAIL_HOST_PASSWORD = '19960213Z26a'
EMAIL_PORT = 465
