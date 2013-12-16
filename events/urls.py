from django.conf.urls import patterns,url

from .views import index, ShowListView

urlpatterns = patterns('',
	url(r'^$',index,name='index'),
	url(r'^shows/$',ShowListView.as_view(),name='show_list'),
	)
