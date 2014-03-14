from django.conf.urls import patterns,url

from .views import CourseListView 
from .views import AddCourse
from .views import EditCourse
from .views import DeleteCourse
from .views import CourseDetail
from .views import LocationDetailView
from .views import ReserveCourse, ReserveCourseThanks
from .views import WaitingListCourse, WaitingListCourseThanks
from .views import UpdateStudent

urlpatterns = patterns('',
	url(r'^list/$',CourseListView.as_view(),name='course_list'),
	url(r'^(?P<pk>\d+)/$',CourseDetail.as_view(),name='course_detail'),	
	url(r'^add/$',AddCourse.as_view(),name='course_create'),
	url(r'^edit/(?P<pk>\d+)/$',EditCourse.as_view(),name='course_edit'),
	url(r'^delete/(?P<pk>\d+)/$',DeleteCourse.as_view(),name='course_delete'),
	url(r'^location/(?P<pk>\d+)/$', LocationDetailView.as_view(),name='location_detail'),
	url(r'^reserve/(?P<pk>\d+)/$', ReserveCourse.as_view(),name='reserve_course'),
	url(r'^thanks/$', ReserveCourseThanks.as_view(),name='course_reservation_thanks'),
	url(r'^waitinglist/(?P<pk>\d+)/$', WaitingListCourse.as_view(),name='course_waitinglist'),
	url(r'^waitinglist_thanks/$', WaitingListCourseThanks.as_view(),name='course_waitinglist_thanks'),
	url(r'^updatestudent/(?P<pk>\d+)/$', UpdateStudent.as_view(),name='update_student'),	
	)
