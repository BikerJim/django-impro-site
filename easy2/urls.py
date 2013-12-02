from django.conf.urls import patterns, include, url

from django.contrib import admin
from . import settings

from home.views import homepage

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', homepage),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/logout/$','django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/',include('allauth.urls')),
    url(r'^events/', include('events.urls')),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$',
        'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
