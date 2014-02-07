from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.mail import EmailMultiAlternatives
from django.views.generic import CreateView, TemplateView
from django.shortcuts import get_object_or_404
from django.template import loader
from django.template import Context
from .models import Reservation
from .forms import ReserveTicketForm
from datetime import date, time, datetime, timedelta
from events.models import Event_date

class ReserveTicket(CreateView):
	model = Reservation
	form_class = ReserveTicketForm
	fields = ('reserved_by','email_address','number_of_tickets','early_show','late_show','promo_code','heard_about')

	def get_form(self, form_class):
		form = super(ReserveTicket, self).get_form(form_class)
		self.event_date = get_object_or_404(Event_date, pk=self.kwargs['pk'])
		form.fields['event_date'].initial = self.event_date.id
		if self.request.user.is_authenticated():
			if self.request.user.first_name and self.request.user.last_name:
				form.fields['reserved_by'].initial = self.request.user.first_name+" "+self.request.user.last_name
			elif self.request.user.first_name:
				form.fields['reserved_by'].initial = self.request.user.first_name
			else:
				form.fields['reserved_by'].initial = self.request.user
			form.fields['email_address'].initial = self.request.user.email
		return form
	
	def form_valid(self, *args, **kwargs):
		form = super(ReserveTicket, self).form_valid(*args, **kwargs)
		self.request.session['res_id'] = self.object.id
		return form

	def get_context_data(self, *args, **kwargs):
		context = super(ReserveTicket, self).get_context_data(*args, **kwargs)
		if (date.today() - self.event_date.date) >= timedelta(-1):
			too_late = True
		else:
			too_late = False
		context['show_date'] = self.event_date
		context['too_late'] = too_late
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
		recipient = [self.reservation.email_address]
		e_message = EmailMultiAlternatives(subject, text_message, 'bookings@easylaughs.nl', recipient)
		e_message.attach_alternative(html_message, "text/html")
		return e_message.send()

	def get_context_data(self, *args, **kwargs):
		pk = self.request.session['res_id']
		self.reservation = Reservation.objects.get(pk=pk)
		context = super(ReserveThanks, self).get_context_data(*args, **kwargs)
		context['date'] = self.reservation.event_date
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
