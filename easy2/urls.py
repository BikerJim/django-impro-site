from django.conf.urls import patterns, include, url

from django.contrib import admin
#import settings.local

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
)

#if not settings.local.DEBUG==True:
#	pass
#else:
    # static files (images, css, javascript, etc.)
#    import debug_toolbar
#    urlpatterns += patterns('',
#        (r'^media/(?P<path>.*)$',
#        'django.views.static.serve', {
#        'document_root': settings.local.MEDIA_ROOT}),
#        url(r'^__debug__/', include(debug_toolbar.urls)),
#    )
