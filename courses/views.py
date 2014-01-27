from django.core.mail import EmailMultiAlternatives

from django.db.models import Q

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import Context, loader

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import TemplateView

from datetime import date, time, datetime

from .models import Course
from .models import Location
from .models import Student

from .forms import CourseSignupForm

class CourseListView(ListView):
	model = Course
	try:
		queryset = Course.objects.filter(show_date__date__gte=datetime.today()).order_by('start_date')
	except IndexError:
		queryset = {}
	 
class AddCourse(CreateView):
	pass
	
class EditCourse(UpdateView):
	pass
	
class DeleteCourse(DeleteView):
	pass
	
class CourseDetail(DetailView):
	model = Course
	def get_context_data(self, **kwargs):
		context = super(CourseDetail, self).get_context_data(**kwargs)
		student_list = Student.objects.filter(course=self.kwargs['pk'])
		registered_list = student_list.filter(Q(status=1) | Q(status=2))
		waiting_list = student_list.filter(status=3)
		is_teacher = self.request.user.groups.filter(name='teacher')
		context['student_list'] = registered_list
		context['waiting_list'] = waiting_list
		context['is_teacher'] = is_teacher
		return context
	
class ReserveCourse(CreateView):
	model = Student
	form_class = CourseSignupForm
	success_url = '/courses/thanks'
	fields = (
			'name',
			'email_address',
			'telephone',
			'heard_about',
			)
			
	def get_form(self, form_class):
		form = super(ReserveCourse, self).get_form(form_class)
		self.course = get_object_or_404(Course, pk=self.kwargs['pk'])
		form.fields['course'].initial = self.course.id
		form.fields['status'].initial = 1
		if self.request.user.is_authenticated():
			if self.request.user.first_name and self.request.user.last_name:
				form.fields['name'].initial = self.request.user.first_name+" "+self.request.user.last_name
			elif self.request.user.first_name:
				form.fields['name'].initial = self.request.user.first_name
			else:
				form.fields['name'].initial = self.request.user
			form.fields['email_address'].initial = self.request.user.email
			form.fields['heard_about'].initial = u'easylaughs account holder'
		return form	

	def form_valid(self, *args, **kwargs):
		form = super(ReserveCourse, self).form_valid(*args, **kwargs)
		self.request.session['student_id'] = self.object.id
		return form

	def get_context_data(self, *args, **kwargs):
		context = super(ReserveCourse, self).get_context_data(*args, **kwargs)
		context['course'] = self.course
		return context

class WaitingListCourse(CreateView):
	model = Student
	form_class = CourseSignupForm
	template_name = 'courses/student_waitinglist_form.html'
	success_url = '/courses/waitinglist_thanks'
	fields = (
			'name',
			'email_address',
			'telephone',
			'heard_about',
			)
			
	def get_form(self, form_class):
		form = super(WaitingListCourse, self).get_form(form_class)
		self.course = get_object_or_404(Course, pk=self.kwargs['pk'])
		form.fields['course'].initial = self.course.id
		form.fields['status'].initial = 3
		if self.request.user.is_authenticated():
			if self.request.user.first_name and self.request.user.last_name:
				form.fields['name'].initial = self.request.user.first_name+" "+self.request.user.last_name
			elif self.request.user.first_name:
				form.fields['name'].initial = self.request.user.first_name
			else:
				form.fields['name'].initial = self.request.user
			form.fields['email_address'].initial = self.request.user.email
			form.fields['heard_about'].initial = u'easylaughs account holder'
		return form	

	def form_valid(self, *args, **kwargs):
		form = super(WaitingListCourse, self).form_valid(*args, **kwargs)
		self.request.session['student_id'] = self.object.id
		return form

	def get_context_data(self, *args, **kwargs):
		context = super(WaitingListCourse, self).get_context_data(*args, **kwargs)
		context['course'] = self.course
		return context

class ReserveCourseThanks(TemplateView):
	"""
	A view to show after a successful reservation, show the details
	and send a confirmation email.
	"""
	template_name="courses/thanks.html"

	def send_confirmation_email(self, context):
		html_template = loader.get_template('courses/conf_email.html')
		text_template = loader.get_template('courses/conf_email.txt') 
		context = Context(context)
		subject = "easylaughs reservation for %s" % context['course']
		html_message = html_template.render(context)
		text_message = text_template.render(context) 
		recipient = [self.student.email_address]
		e_message = EmailMultiAlternatives(subject, text_message, 'courses@easylaughs.nl', recipient)
		e_message.attach_alternative(html_message, "text/html")
		return e_message.send()

	def get_context_data(self, *args, **kwargs):
		pk = self.request.session['student_id']
		self.student = Student.objects.get(pk=pk)
		context = super(ReserveCourseThanks, self).get_context_data(*args, **kwargs)
		context['course'] = self.student.course
		context['student'] = self.student.name
		self.send_confirmation_email(context)
		return context

class WaitingListCourseThanks(TemplateView):
	"""
	A view to show after a successful waitinglist request,
	show the details and send a confirmation email.
	"""
	template_name="courses/waitinglist_thanks.html"

	def send_confirmation_email(self, context):
		html_template = loader.get_template('courses/waitinglist_email.html')
		text_template = loader.get_template('courses/waitinglist_email.txt') 
		context = Context(context)
		subject = "easylaughs waiting list: %s" % context['course']
		html_message = html_template.render(context)
		text_message = text_template.render(context) 
		recipient = [self.student.email_address]
		e_message = EmailMultiAlternatives(subject, text_message, 'courses@easylaughs.nl', recipient)
		e_message.attach_alternative(html_message, "text/html")
		return e_message.send()

	def get_context_data(self, *args, **kwargs):
		pk = self.request.session['student_id']
		self.student = Student.objects.get(pk=pk)
		context = super(WaitingListCourseThanks, self).get_context_data(*args, **kwargs)
		context['course'] = self.student.course
		context['student'] = self.student.name
		self.send_confirmation_email(context)
		return context

class LocationDetailView(DetailView):
	model = Location
