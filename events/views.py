from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Show
from .models import Workshop
from .models import Event_date

from datetime import date, time, datetime
from .forms import AddShowForm, EditShowForm
from .forms import AddWorkshopForm, EditWorkshopForm

from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

class ShowListView(ListView):
	model = Show
	try:
		queryset = Show.objects.all().filter(date__date__gte=datetime.today()).order_by('date','date__event_type')
	except IndexError:
		queryset = {}
	
#	def get_context_data(self, **kwargs):
#		context = super(ShowListView, self).get_context_data(**kwargs)
#		return context

class AddShow(CreateView):
	model = Show
	form_class = AddShowForm
	template_name = 'events/show_create.html'
	
	@method_decorator(permission_required('events.add_show', raise_exception=True))
	def dispatch(self, *args, **kwargs):
		response = super(AddShow, self).dispatch(*args, **kwargs)
		return response
		
	def form_valid(self, form):
		ev_date = Event_date.objects.get(pk=self.request.POST[u'date'])
		ev_date.taken = True
		ev_date.save()
		return super(AddShow, self).form_valid(form)
		
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
	
	def post(self, *args, **kwargs):
		show_id = self.kwargs['pk']
		show = Show.objects.get(pk=show_id)
		ev_date = Event_date.objects.get(pk=show.date.id)
		ev_date.taken = False
		ev_date.save()
		return super(DeleteShow, self).post(*args, **kwargs)
	
	def get_success_url(self):
		return reverse_lazy('show_list')

class WorkshopListView(ListView):
	model = Workshop
	try:
		queryset = Workshop.objects.all().filter(date__date__gte=datetime.today()).order_by('date')
	except IndexError:
		queryset = {}
	
	def get_context_data(self, **kwargs):
		context = super(WorkshopListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

class AddWorkshop(CreateView):
	model = Workshop
	form_class = AddWorkshopForm
	template_name = 'events/workshop_create.html'
	
	@method_decorator(permission_required('events.add_workshop', raise_exception=True))
	def dispatch(self, *args, **kwargs):
		response = super(AddWorkshop, self).dispatch(*args, **kwargs)
		return response
		
	def form_valid(self, form):
		ev_date = Event_date.objects.get(pk=self.request.POST[u'date'])
		ev_date.taken = True
		ev_date.save()
		return super(AddWorkshop, self).form_valid(form)	
	
	def get_success_url(self):
		return reverse('workshop_list')
		
class EditWorkshop(UpdateView):
	model = Workshop
	form_class = EditWorkshopForm
	template_name = 'events/workshop_edit.html'
	
	@method_decorator(permission_required('events.change_workshop', raise_exception=True))
	def dispatch(self, *args, **kwargs):
		response = super(EditWorkshop, self).dispatch(*args, **kwargs)
		return response
	
	def get_success_url(self):
		return reverse('workshop_list')	
	
class DeleteWorkshop(DeleteView):
	model = Workshop
	template_name = 'events/workshop_delete.html'
	
	@method_decorator(permission_required('events.delete_workshop', raise_exception=True))
	def dispatch(self, *args, **kwargs):
		response = super(DeleteWorkshop, self).dispatch(*args, **kwargs)
		return response
		
	def post(self, *args, **kwargs):
		ws_id = self.kwargs['pk']
		ws = Workshop.objects.get(pk=ws_id)
		ev_date = Event_date.objects.get(pk=ws.date.id)
		ev_date.taken = False
		ev_date.save()
		return super(DeleteWorkshop, self).post(*args, **kwargs)

	def get_success_url(self):
		return reverse('workshop_list')
