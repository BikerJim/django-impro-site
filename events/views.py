from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Show

from datetime import date, time, datetime
from .forms import AddShowForm, EditShowForm

from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

class ShowListView(ListView):
	model = Show
	try:
		queryset = Show.objects.all().filter(date__date__gte=datetime.today()).order_by('date')
	except IndexError:
		queryset = {}
	
	def get_context_data(self, **kwargs):
		context = super(ShowListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

class AddShow(CreateView):
	model = Show
	form_class = AddShowForm
	template_name = 'events/show_create.html'
	
	@method_decorator(permission_required('events.add_show', raise_exception=True))
	def dispatch(self, *args, **kwargs):
		response = super(AddShow, self).dispatch(*args, **kwargs)
		return response
	
	def get_success_url(self):
		return reverse('show_list')
		
class EditShow(UpdateView):
	model = Show
	form_class = EditShowForm
	template_name = 'events/show_edit.html'
	
	@method_decorator(permission_required('events.change_show', raise_exception=True))
	def dispatch(self, *args, **kwargs):
		response = super(EditShow, self).dispatch(*args, **kwargs)
		return response
	
	def get_success_url(self):
		return reverse('show_list')	
	
class DeleteShow(DeleteView):
	model = Show
	template_name = 'events/show_delete.html'
	
	@method_decorator(permission_required('events.delete_show', raise_exception=True))
	def dispatch(self, *args, **kwargs):
		response = super(DeleteShow, self).dispatch(*args, **kwargs)
		return response
	
	def get_success_url(self):
		return reverse('show_list')
