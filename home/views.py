from django.shortcuts import render
from django.utils.timezone import utc

from django.views.generic.list import ListView

from events.models import Show, Event_date

from datetime import date, time, datetime


class Index(ListView):
	model = Show
	context_object_name = 'index'
	template_name = 'home/index.html'
	now = date.today()
	queryset= Event_date.objects.filter(date__gte=now)
	
	def dispatch(self, request, *args, **kwargs):
		response = super(Index, self).dispatch(request, *args, **kwargs)
		print "request.GET: %s" % (request.GET)
		print self.now
		print self.queryset
		return response
	
	def get_context_data(self,**kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context['greeting'] = "Hey I am being passed through from the view"
		return context
	
