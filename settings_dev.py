import os
from settings_common import *

IS_DEV = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

if not IS_TEST:
    LOGGING['handlers']['console']['level'] = 'DEBUG'
    LOGGING['loggers']['']['level'] = 'DEBUG'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# For user-supplied content
MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')
MEDIA_URL = '/media/'

# For developer-supplied content
STATIC_ROOT = os.path.join(ROOT_DIR, 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            '127.0.0.1:11211',
        ],
        'TIMEOUT': 86400,
    }
}


##################################################
##########  Django Toolbar Settings     ##########
##################################################

INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

DEFAULT_DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
]

DEBUG_TOOLBAR_PANELS = DEFAULT_DEBUG_TOOLBAR_PANELS


##################################################
##########  Analytics Settings          ##########
##################################################

# GA Settings
GOOGLE_ANALYTICS_CODE = ''

# KISSMetrics Settings
KISSMETRICS_API_KEY = 'asdf'
KISSMETRICS_TRACK_INTERNALLY = True