import os
import sys

if sys.argv and len(sys.argv) > 1:
    IS_TEST = 'test' == sys.argv[1]
else:
    IS_TEST = False

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

vet24seven_settings = {}
for kv in os.environ.get('VET24SEVEN_SETTINGS').split('&'):
    a = kv.split('=')
    vet24seven_settings[a[0]] = a[1]

DB_ENGINE = 'django.db.backends.postgresql_psycopg2'
DB_HOST = vet24seven_settings['DB_HOST']
DB_NAME = vet24seven_settings['DB_NAME']
DB_PASSWORD = vet24seven_settings['DB_PASSWORD']
DB_USER = vet24seven_settings['DB_USER']

LOGIN_URL = '/existing/'

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

####
# AWS Settings
####

AWS_ACCESS_KEY_ID = vet24seven_settings['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = vet24seven_settings['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = vet24seven_settings['AWS_STORAGE_BUCKET_NAME']
AWS_BUCKET_URL = u'http://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
AWS_QUERYSTRING_AUTH = False
AWS_QUERYSTRING_EXPIRE = 31556926
AWS_HEADERS = {
         'x-amz-acl': 'public-read',
         'Expires': 'Sat, 30 Oct 2020 20:00:00 GMT',
         'Cache-Control': 'public, max-age=31556926'
}

# boto settings
S3_SETTINGS = {
    'aws_key': AWS_ACCESS_KEY_ID,
    'aws_secret_key': AWS_SECRET_ACCESS_KEY,
    'bucket': AWS_STORAGE_BUCKET_NAME,
    'default_perm': 'public-read',
    'vanity_url': False
}

DEFAULT_CHARSET = 'utf-8'

LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
                'verbose': {
                        'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
                },
                'simple': {
                        'format': '%(levelname)s %(message)s'
                },
        },
        'handlers': {
                'null': {
                        'level': 'DEBUG',
                        'class': 'django.utils.log.NullHandler',
                },
                'console':{
                        'level': 'INFO',
                        'class': 'logging.StreamHandler',
                        'formatter': 'verbose'
                },
                'mail_admins': {
                        'level': 'ERROR',
                        'class': 'django.utils.log.AdminEmailHandler'
                },
        },
        'loggers': {
                '': {
                        'handlers': ['console'],
                        'propagate': True,
                        'level': 'INFO',
                },
                'django': {
                        'handlers': ['console'],
                        'propagate': True,
                        'level': 'INFO',
                },
                'django.request': {
                        'handlers': ['mail_admins', 'console'],
                        'level': 'ERROR',
                        'propagate': True,
                },
                'django.db.backends': {
                        'handlers': ['mail_admins', 'console'],
                        'level': 'ERROR',
                        'propagate': True,
                },
                'upvote': {
                        'handlers': ['console', 'mail_admins'],
                        'level': 'INFO'
                }
        }
}