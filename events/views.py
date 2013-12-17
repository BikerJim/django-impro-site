from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone

from django.views.generic.list import ListView

from .models import Show

class ShowListView(ListView):
	model = Show
	def get_context_data(self, **kwargs):
		context = super(ShowListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context
