from django.conf.urls import patterns, include, url

from django.contrib import admin
from home.views import homepage
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', homepage),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('allauth.urls')),
)
