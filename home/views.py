from django.shortcuts import render
from django.utils.timezone import utc

from django.views.generic.list import ListView

from events.models import Show, Workshop

from allauth.account.models import UserProfile

from datetime import date, time, datetime
from operator import attrgetter
from itertools import chain

class Index(ListView):
	model = Show
	context_object_name = 'index'
	template_name = 'home/index.html'
	now = date.today()
	
	def get_next_event(self,model,event_type):
		self.model = model
		self.event_type = event_type
		try:
			return model.objects.filter(date__event_type=event_type).\
			filter(date__date__gte=datetime.today()).earliest('date')
		except model.DoesNotExist:
			return False
	
	def get_queryset(self):
		self.next_show = self.get_next_event(Show,1)
		self.next_workshop = self.get_next_event(Workshop,2)
		queryset = [self.next_show, self.next_workshop]
		return queryset
				
	def get_context_data(self,**kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context['show'] = self.next_show
		context['workshop'] = self.next_workshop
		return context
	
class AboutUs(ListView):
	model = UserProfile
	template_name = 'home/about_us.html'
	queryset = UserProfile.objects.filter(user__groups=2).order_by('user__first_name')
