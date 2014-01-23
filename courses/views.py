from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import TemplateView

from datetime import date, time, datetime

from .models import Course
from .models import Location

class CourseListView(ListView):
	model = Course
	try:
		queryset = Course.objects.filter(show_date__date__gte=datetime.today()).order_by('start_date')
	except IndexError:
		queryset = {}
	 
class AddCourse(CreateView):
	pass
	
class EditCourse(UpdateView):
	pass
	
class DeleteCourse(DeleteView):
	pass
	
class CourseDetail(DetailView):
	model = Course
	
class CourseReservation(TemplateView):
	pass

class LocationDetailView(DetailView):
	model = Location
