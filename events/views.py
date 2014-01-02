from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.utils import timezone
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Show
from .models import Workshop
from .models import Event_date
from .models import Availability
from allauth.utils import get_user_model

from datetime import date, time, datetime
from .forms import AddShowForm, EditShowForm
from .forms import AddWorkshopForm, EditWorkshopForm
from .forms import UpdateAvailabilityForm

from django.views.generic.edit import FormMixin

from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

class ShowListView(ListView):
	model = Show
	try:
		queryset = Show.objects.all()\
		.filter(date__date__gte=datetime.today())\
		.order_by('date','date__event_type')
	except IndexError:
		queryset = {}

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

class FormListView(FormMixin, ListView):
	def get_queryset(self):
		event_type_list = range(5)
		datelist = Event_date.objects\
		.filter(date__gte=datetime.today())\
		.filter(event_type__in=event_type_list)\
		.order_by('date','event_type')
		person = self.request.user
		for date in datelist:
			Availability.objects.get_or_create(
			date = date,
			person = person,
			defaults = {'available': False})
		queryset = Availability.objects.filter(person=person)\
			.filter(date__date__gte=datetime.today())\
			.order_by('date', 'date__event_type')
		return queryset

	def get(self, request, *args, **kwargs):
		# From ProcessFormMixin
		form_class = self.get_form_class()
		self.form = self.get_form(form_class)

		# From BaseListView
		self.object_list = self.get_queryset()
		allow_empty = self.get_allow_empty()
		if not allow_empty and len(self.object_list) == 0:
			raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
						% {'class_name': self.__class__.__name__})

		context = self.get_context_data(object_list=self.object_list, form=self.form)
		return self.render_to_response(context)		

	def post(self, request, *args, **kwargs):
		av_list = self.request.POST.getlist("available")
		nav_list = self.request.POST.getlist("notavailable")
		Availability.objects.filter(id__in=av_list).update(available=True)
		Availability.objects.filter(id__in=nav_list).update(available=False)
		return self.get(request, *args, **kwargs)

		
class AvailabilityList(FormListView):
	form_class = UpdateAvailabilityForm
	Model = Availability
	paginate_by = 10
		
	@method_decorator(permission_required('events.change_availability', raise_exception=True))
	def dispatch(self, *args, **kwargs):
		response = super(AvailabilityList, self).dispatch(*args, **kwargs)
		return response
