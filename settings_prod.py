from settings_common import *

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': ['127.0.0.1:11211'],
        'TIMEOUT': 86400,
        }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# For user-supplied content
MEDIA_URL = AWS_BUCKET_URL

# For developer-supplied content
STATIC_ROOT = os.path.join(ROOT_DIR,'static')
STATIC_URL = u'%s/' % os.path.join(AWS_BUCKET_URL, u'static')
ADMIN_MEDIA_PREFIX = u'%sadmin/' % STATIC_URL

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'