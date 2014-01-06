from django import forms
from django.forms import ModelForm

from booking.models import Reservation

class ReserveTicketForm(forms.ModelForm):
	
	class Meta:
		model = Reservation
		fields = [
			'number_of_tickets',
			'early_show',
			'late_show',
			'promo_code',
			'heard_about',
			'reserved_by',
			'email_address',
			'event_date']
