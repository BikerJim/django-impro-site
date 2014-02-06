from django.conf.urls import patterns, url

urlpatterns = patterns(
	'api.views',
	url(r'^next_show/$', 'next_show', name='next_show'),
)
