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
		
		if len(self.next_early_show) > 0:
			self.next_early_show = self.next_early_show[0]
			print "Early: %s" % self.next_early_show.date.date
			print "Late: %s" % self.next_late_show.date.date
			if self.next_early_show.date.date > self.next_late_show.date.date:
				self.next_early_show = {}
			elif self.next_early_show.date.date < self.next_late_show.date.date:
				self.next_late_show = {}
				
		if len(self.next_workshop) > 0:
			self.next_workshop = self.next_workshop[0]
		
		if self.next_early_show:	
			self.show_id = self.next_early_show.date.id
		elif self.next_late_show:
			self.show_id = self.next_late_show.date.id
		
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
	
