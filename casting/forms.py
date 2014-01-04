from django import forms
from django.forms import ModelForm

from events.models import Availability

class CastingForm(forms.ModelForm):

	class Meta:
		model = Availability
		fields = ['date','person','available','cast','host']
