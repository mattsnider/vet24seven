import logging
from settings_common import *

IS_DEV = False
DEBUG = False


##################################################
##########          Django Settings     ##########
##################################################

DEBUG = False

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
#TIME_ZONE = 'America/Los Angeles'
TIME_ZONE = 'UTC' # changed to UTC

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = vet24seven_settings['SECRET_KEY']

# Temp directory
TMP_DIR = os.path.join(ROOT_DIR,'tmp')

# Directory of main django template files.
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_DIR, 'templates'),
    )

#FIXTURE_DIRS = (path.join(ROOT_DIR, 'service_zipcode', 'fixtures'),)

# facebook needs to be last for this to work
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
    )

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #        'django.template.loaders.eggs.load_template_source',
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'homepage.context_processors.shared_context',
    )

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    ]

ROOT_URLCONF = 'urls'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.auth',
    'django.contrib.staticfiles',
    'south',
    'django_shared',
    'homepage',
    ]

ADMINS = (
    ('Errors', 'errors@mattsnider.com',),
    )

DATABASES = {
    'default': {
        'NAME': DB_NAME,
        'ENGINE': DB_ENGINE,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
    },
}

MANAGERS = ADMINS

SOUTH_TESTS_MIGRATE = False # so that south doesn't interfere with tests

APPEND_SLASH = True

CACHE_PREFIX = 'vet24seven:'
SIMPLE_CACHE_SECONDS = 300 # duration of cached variables

SITE_ID = 1

DEFAULT_FROM_EMAIL = 'Matt Snider <admin@mattsnider.com>'
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

STATIC_FILE_COMBINATIONS = {}

if vet24seven_settings['ENV'] == 'prod':
    from settings_prod import *
elif vet24seven_settings['ENV'] == 'dev':
    from settings_dev import *
else:
    logging.error('VET24SEVEN_SETTINGS does not define an env value.')

try:
    from settings_local import *
except Exception, e:
    logging.info('No settings_local.py, nothing overridden.')

if IS_TEST:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # Force test cache values into a test- namespace
    try:
        for alias in CACHES.keys():
            cache_settings = CACHES[alias]
            old_value = cache_settings.get('KEY_PREFIX', '')
            cache_settings['KEY_PREFIX'] = 'test-%s' % old_value
    except NameError:
        if not IS_DEV:
            raise
else:
    # remove some stuff from test
    MIDDLEWARE_CLASSES.append('django.middleware.csrf.CsrfViewMiddleware')