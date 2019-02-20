import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'mysql',
        'PORT': '3306',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',

        }
    }
}

MEMCACHED_HOST = os.environ.get('MEMCACHED_HOST') or '127.0.0.1'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '%s:11211' % MEMCACHED_HOST,
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'


DEBUG = False




