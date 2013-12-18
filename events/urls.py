from django.conf.urls import patterns,url

from .views import ShowListView, AddShow, EditShow, DeleteShow

urlpatterns = patterns('',
	url(r'^shows/$',ShowListView.as_view(),name='show_list'),
	url(r'^shows/add/$',AddShow.as_view(),name='show_create'),
	url(r'^shows/edit/(?P<pk>\d+)/$',EditShow.as_view(),name='show_edit'),
	url(r'^shows/delete/(?P<pk>\d+)/$',DeleteShow.as_view(),name='show_delete'),
	)
