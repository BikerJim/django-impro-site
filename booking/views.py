from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.mail import EmailMultiAlternatives
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.template import loader
from django.template import Context
from .models import Reservation
from .forms import ReserveTicketForm
from datetime import date, time, datetime
from events.models import Event_date

class ReserveTicket(CreateView):
	model = Reservation
	form_class = ReserveTicketForm
	fields = ('number_of_tickets','early_show','late_show','promo_code','heard_about')

	@method_decorator(login_required())
	def dispatch(self, *args, **kwargs):
		response = super(ReserveTicket, self).dispatch(*args, **kwargs)
		return response

	def get_form(self, form_class):
		form = super(ReserveTicket, self).get_form(form_class)
		self.event_date = get_object_or_404(Event_date, pk=self.kwargs['pk'])
		form.fields['reserved_by'].initial = self.request.user
		form.fields['event_date'].initial = self.event_date.date
		return form

	def get_context_data(self, *args, **kwargs):
		context = super(ReserveTicket, self).get_context_data(*args, **kwargs)
		context['show_date'] = self.event_date
		return context

class ReserveThanks(TemplateView):
	"""
	A view to show after a successful reservation, show the details
	and send a confirmation email.
	"""
	template_name="booking/thanks.html"

	def send_confirmation_email(self, context):
		html_template = loader.get_template('booking/conf_email.html')
		text_template = loader.get_template('booking/conf_email.txt') 
		context = Context(context)
		subject = "easylaughs reservation for %s" % context['date'].date
		html_message = html_template.render(context)
		text_message = text_template.render(context) 
		recipient = [self.request.user.email]
		e_message = EmailMultiAlternatives(subject, text_message, 'bookings@easylaughs.nl', recipient)
		e_message.attach_alternative(html_message, "text/html")
		return e_message.send()

	def get_context_data(self, *args, **kwargs):
		self.reservation = Reservation.objects.filter(reserved_by=self.request.user).latest('created_date')
		context = super(ReserveThanks, self).get_context_data(*args, **kwargs)
		context['date'] = Event_date.objects.get(event_type=2,date=self.reservation.event_date)
		context['tickets'] = self.reservation.number_of_tickets
		context['student_cash'] = 4*self.reservation.number_of_tickets
		if self.reservation.early_show and self.reservation.late_show:
			context['shows'] = 'both shows'
			context['cash'] = 10*self.reservation.number_of_tickets
		elif self.reservation.early_show and not self.reservation.late_show:
			context['shows'] = 'the early show'
			context['cash'] = 5*self.reservation.number_of_tickets
		elif self.reservation.late_show and not self.reservation.early_show:
			context['shows'] = 'the late show'
			context['cash'] = 10*self.reservation.number_of_tickets
		self.send_confirmation_email(context)
		return context
	

