from django.conf import settings
from django.conf.urls import patterns, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import redirect_to

admin.autodiscover()

urlpatterns = patterns('',
    # serving static files
    (r'^favicon\.ico$', redirect_to, {'url': '/static/image/icon/favicon.ico'}),
    (r'^apple-touch-icon\.png$', redirect_to, {'url': '/static/image/icon/apple-touch-icon.png'}),

    # django stuff
#    (r'^robots.txt$', include('robots.urls')),
#    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemaps}),
#    (r'^sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # project URLs
#    (r'^/', include('diablo.urls', namespace='diablo')),

    # error pages
#    (r'^404/$', 'common.views.page_not_found'),
#    (r'^500/$', 'common.views.server_error'),
)

urlpatterns += patterns('homepage.views',
    url(r'^email/$', 'email', name='email'),
    url(r'^$', 'index', name='index'),
)

handler404 = 'common.views.page_not_found'
handler500 = 'common.views.server_error'

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()