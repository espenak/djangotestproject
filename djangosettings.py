DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (('SuperHero', 'superman@example.com'),)
MANAGERS = ADMINS
SERVER_EMAIL = 'superman@example.com'
DEFAULT_FROM_EMAIL = 'superman@example.com'
SECRET_KEY = ')b9a1=mfqx++v=vk8m*u+zteqq$-s6s@sda@+2^(76j2254l9y'
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'
STATIC_ROOT = 'static'
STATIC_URL = '/static/'
INTERNAL_IPS = ('127.0.0.1',)
SEND_EMAIL = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ROOT_URLCONF = 'djangourls'

INSTALLED_APPS = [
    'my_example'
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s %(asctime)s %(name)s %(pathname)s:%(lineno)s] %(message)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },

    'handlers': {
        'stderr': {
            'level': 'DEBUG',
            'formatter': 'verbose',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['stderr'],
            'level': 'ERROR',
            'propagate': False
        },
        'django.db': {
            'handlers': ['stderr'],
            'level': 'INFO', # Set to DEBUG to see all sql queries
            'propagate': False
        },
        '': {
            'handlers': ['stderr'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}
