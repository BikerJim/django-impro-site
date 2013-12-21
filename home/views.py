from django.shortcuts import render
from django.utils.timezone import utc

from django.views.generic.list import ListView

from events.models import Show, Workshop

from allauth.account.models import UserProfile

from datetime import date, time, datetime


class Index(ListView):
	model = Show
	context_object_name = 'index'
	template_name = 'home/index.html'
	now = date.today()
	try:
		next_early_show = Show.objects.all().filter(date__date__gte=now).filter(date__event_type=1)[:1].get()
	except Show.DoesNotExist:
		next_early_show = {}
	try:
		next_late_show = Show.objects.all().filter(date__date__gte=now).filter(date__event_type=2)[:1].get()
	except Show.DoesNotExist:
		next_late_show = {}
		
	if next_early_show.date.date > next_late_show.date.date:
		next_early_show = {}
		
	try:
		next_workshop = Workshop.objects.all().filter(date__date__gte=now).filter(date__event_type=3)[:1].get()
	except Workshop.DoesNotExist:
		next_workshop = {}
	
	def get_context_data(self,**kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context['early'] = self.next_early_show
		context['late'] = self.next_late_show
		context['workshop'] = self.next_workshop
		return context
	
class AboutUs(ListView):
	model = UserProfile
	template_name = 'home/about_us.html'
	queryset = UserProfile.objects.filter(user__groups=2)
	
