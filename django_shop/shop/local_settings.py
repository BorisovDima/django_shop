

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_shop',
        'USER': 'root',
        'PASSWORD': '1488',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        }
    }
}


STATIC_ROOT = '/var/www/shopdjango.ru/static'


CART_SESSION_KEY = 'orders_'
ORDER_SESSION_ID = 'order_id'

MAX_CART_SIZE = 100

PAYPAL_RECEIVER_EMAIL = 'dmitriy_shvidkiy@mail.ru'
PAYPAL_TEST = True


SESSION_COOKIE_AGE = 1209600



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

######### form ###########################

CRISPY_TEMPLATE_PACK = 'bootstrap4'

################### pay #####################

CUR_CURRENCY = '$'

CUR_CURRENCY_COD = 'USD'

################# admin ###############


ADMIN_DATE_FORMAT = '%d/%m/%Y %H.%M'