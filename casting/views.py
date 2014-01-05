from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from events.models import Show, Availability

from .forms import CastingForm

class CastShowListForm(FormMixin, ListView):
	def get_queryset(self):
		self.queryset = Availability.objects.filter(date=self.show.date).filter(available=True)
		self.actor_count = self.queryset.count()
		return self.queryset
		
	def available_actors(self):
		show = Show.objects.get(pk=self.kwargs['pk'])
		av_actors = Availability.objects.filter(date=show.date).filter(available=True)
		return av_actors
		
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
		av_actors = self.available_actors()
		cast_list = self.request.POST.getlist("cast")
		host_list = self.request.POST.getlist("host")
		id_list = []
		not_cast = []
		not_host = []
				
		for actor in av_actors:
			id_list.append(unicode(actor.id))
			
		for act_id in id_list:
			if act_id not in cast_list:
				not_cast.append(act_id)
			if act_id not in host_list:
				not_host.append(act_id)
		Availability.objects.filter(id__in=not_cast).update(cast=False)
		Availability.objects.filter(id__in=not_host).update(host=False)
		Availability.objects.filter(id__in=cast_list).update(cast=True)
		Availability.objects.filter(id__in=host_list).update(host=True)
		return HttpResponseRedirect('/casting/done/')
		
	def get_form(self, form_class):
		self.form = super(CastShowListForm, self).get_form(form_class)
		self.show = get_object_or_404(Show, pk=self.kwargs['pk'])
		self.form.fields['date'].initial = self.show.date
		return self.form
		
	def get_context_data(self, *args, **kwargs):
		context = super(CastShowListForm, self).get_context_data(*args, **kwargs)
		context['show'] = self.show
		context['available_actors'] = self.get_queryset
		context['actor_count'] = self.actor_count
		context['min_actors'] = self.show.late_show.min_actors
		context['max_actors'] = self.show.late_show.max_actors
		return context
		
class CastShow(CastShowListForm):
	model = Availability
	form_class = CastingForm
	template_name="casting/cast_form.html"
	
	fields = ['date','person','available','cast','host']

	@method_decorator(permission_required('events.change_availability', raise_exception=True))
	def dispatch(self, *args, **kwargs):
		response = super(CastShow, self).dispatch(*args, **kwargs)
		return response
	
		
class CastShowDone(TemplateView):
	template_name="casting/done.html"
