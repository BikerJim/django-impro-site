from django import forms
from django.forms import ModelForm

from booking.models import Reservation

class ReserveTicketForm(forms.ModelForm):

	class Meta:
		model = Reservation
