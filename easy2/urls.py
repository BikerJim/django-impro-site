from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings

from home.views import Index, AboutUs

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', AboutUs.as_view(), name='about_us'),
    (r'^accounts/logout/$','django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/',include('allauth.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^booking/', include('booking.urls')),
    url(r'^casting/', include('casting.urls')),
)
if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views', {'document_root': settings.STATIC_ROOT}),
    )
