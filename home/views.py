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
	
	def get_queryset(self):
		self.next_early_show = Show.objects.filter(date__event_type=1).filter(date__date__gte=self.now).order_by('date')
		self.next_late_show = Show.objects.filter(date__event_type=2).filter(date__date__gte=self.now).order_by('date')
		self.next_workshop = Workshop.objects.filter(date__event_type=3).filter(date__date__gte=self.now).order_by('date')
				
		if len(self.next_late_show) > 0:
			self.next_late_show = self.next_late_show[0]
		else:
			self.next_late_show = {}
		
		if len(self.next_early_show) > 0:
			self.next_early_show = self.next_early_show[0]
			if self.next_early_show.date.date > self.next_late_show.date.date:
				self.next_early_show = {}
				
		
		if len(self.next_workshop) > 0:
			self.next_workshop = self.next_workshop[0]
		else:
			self.next_workshop = {}
		
		queryset = chain(self.next_early_show, self.next_late_show, self.next_workshop)
		
		return queryset
		
#	try:
#		next_early_show = Show.objects.filter(date__date__gte=now).filter(date__event_type=1)[:1].get()
#	except Show.DoesNotExist:
#		next_early_show = {}
#	try:
#		next_late_show = Show.objects.filter(date__date__gte=now).filter(date__event_type=2)[:1].get()
#	except Show.DoesNotExist:
#		next_late_show = {}
#	if next_early_show.date.date > next_late_show.date.date:
#		next_early_show = {}
#		
#	workshop_list = Workshop.objects.filter(date__date__gte=now).filter(date__event_type=3).order_by('date')
#	print workshop_list
#	if len(workshop_list) > 0:
#		next_workshop = workshop_list[0]
#	else:
#		next_workshop = {}
				
	def get_context_data(self,**kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context['early'] = self.next_early_show
		context['late'] = self.next_late_show
		context['workshop'] = self.next_workshop
#		context['workshop_list'] = self.workshop_list
		return context
	
class AboutUs(ListView):
	model = UserProfile
	template_name = 'home/about_us.html'
	queryset = UserProfile.objects.filter(user__groups=2)
	
