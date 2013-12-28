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
			return model.objects.filter(date__event_type=event_type).filter(date__date__gte=self.now).order_by('date')[0]
		except IndexError:
			return 0
	
	def get_queryset(self):
		self.next_early_show = self.get_next_event(Show,1)
		self.next_late_show = self.get_next_event(Show,2)
		self.next_workshop = self.get_next_event(Workshop,3)
		
		if self.next_early_show != 0 and self.next_late_show != 0:
			early_show_date = self.next_early_show.date.date
			late_show_date = self.next_late_show.date.date
			if early_show_date > late_show_date:
				self.show_id = self.next_late_show.date.id
				self.next_early_show = {}
			elif early_show_date < late_show_date:
				self.show_id = self.next_early_show.date.id
				self.next_late_show = {}
			else:
				self.show_id = self.next_early_show.date.id
		elif self.next_early_show != 0:
			self.show_id = self.next_early_show.date.id
		elif self.next_late_show != 0:
			self.show_id = self.next_late_show.date.id
		else:
			self.show_id = 0
		
		queryset = chain(self.next_early_show, self.next_late_show, self.next_workshop, self.show_id)
		return queryset
				
	def get_context_data(self,**kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context['early'] = self.next_early_show
		context['late'] = self.next_late_show
		context['workshop'] = self.next_workshop
		context['show_id'] = self.show_id
		return context
	
class AboutUs(ListView):
	model = UserProfile
	template_name = 'home/about_us.html'
	queryset = UserProfile.objects.filter(user__groups=2)
	
