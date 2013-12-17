from django.conf.urls import patterns,url

from .views import ShowListView

urlpatterns = patterns('',
	url(r'^shows/$',ShowListView.as_view(),name='show_list'),
	)
