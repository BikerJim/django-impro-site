from django.conf.urls import patterns,url

from .views import CourseListView 
from .views import AddCourse
from .views import EditCourse
from .views import DeleteCourse
from .views import CourseDetail
from .views import LocationDetailView

urlpatterns = patterns('',
	url(r'^$',CourseListView.as_view(),name='course_list'),
	url(r'^(?P<pk>\d+)/$',CourseDetail.as_view(),name='course_detail'),	
	url(r'^add/$',AddCourse.as_view(),name='course_create'),
	url(r'^edit/(?P<pk>\d+)/$',EditCourse.as_view(),name='course_edit'),
	url(r'^delete/(?P<pk>\d+)/$',DeleteCourse.as_view(),name='course_delete'),
	url(r'^location/(?P<pk>\d+)/$', LocationDetailView.as_view(),name='location_detail'),
	)
