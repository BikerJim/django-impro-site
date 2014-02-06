from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings

from home.views import Index, AboutUs

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^api/', include('api.urls')),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^easylaughsrearend/', include(admin.site.urls)),
    url(r'^about/', AboutUs.as_view(), name='about_us'),
    (r'^accounts/logout/$','django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/',include('allauth.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^booking/', include('booking.urls')),
    url(r'^casting/', include('casting.urls')),
    url(r'^courses/', include('courses.urls')),
)
