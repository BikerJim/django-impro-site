from django.conf.urls import patterns,url

from .views import ShowListView, AddShow, EditShow, DeleteShow, ShowDetail
from .tables import shoverview
from .views import WorkshopListView, AddWorkshop, EditWorkshop, DeleteWorkshop
from .views import AvailabilityList

urlpatterns = patterns('',
	url(r'^shoverview/$','events.tables.shoverview', name='shoverview'),
#	url(r'^shoverview/$',Shoverview.as_view(template_name='events/shoverview.html'),name='shoverview'),
	url(r'^shows/$',ShowListView.as_view(),name='show_list'),
	url(r'^shows/(?P<pk>\d+)/$',ShowDetail.as_view(),name='show_detail'),	
	url(r'^shows/add/$',AddShow.as_view(),name='show_create'),
	url(r'^shows/edit/(?P<pk>\d+)/$',EditShow.as_view(),name='show_edit'),
	url(r'^shows/delete/(?P<pk>\d+)/$',DeleteShow.as_view(),name='show_delete'),
	url(r'^workshops/$',WorkshopListView.as_view(),name='workshop_list'),
	url(r'^workshops/add/$',AddWorkshop.as_view(),name='workshop_create'),
	url(r'^workshops/edit/(?P<pk>\d+)/$',EditWorkshop.as_view(),name='workshop_edit'),
	url(r'^workshops/delete/(?P<pk>\d+)/$',DeleteWorkshop.as_view(),name='workshop_delete'),
	url(r'^availability/$',AvailabilityList.as_view(),name='availability_list'),
	)
