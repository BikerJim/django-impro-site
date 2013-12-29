from django.conf.urls import patterns, include, url

from django.contrib import admin
from settings.base import MEDIA_ROOT

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
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': MEDIA_ROOT}),
)

#        (r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.local.MEDIA_ROOT}),

#<<<<<<< HEAD
#<<<<<<< HEAD
#if not settings.local.DEBUG:
#    pass
#else:
#=======
#if not settings.local.DEBUG==False:
#=======
#if not DEBUG==True:
#>>>>>>> 60b488eb7b6fe6ce8d1982054bb467393908977a
#	pass
#else:
#>>>>>>> be2877c1f769818eeedda4cff2a5dbe9f4ba1037
    # static files (images, css, javascript, etc.)
#    import debug_toolbar
#    urlpatterns += patterns('',
#        url(r'^__debug__/', include(debug_toolbar.urls)),
#    )
