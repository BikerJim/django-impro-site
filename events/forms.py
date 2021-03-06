from django import forms
from django.forms import ModelForm

from .models import Show, Workshop
from .models import Availability

class AddShowForm(forms.ModelForm):

	class Meta:
		model = Show
		fields = [
			'date',
			'early_show',
			'early_extra_inf',
			'late_show',
			'late_extra_inf',]

class EditShowForm(forms.ModelForm):

	class Meta:
		model = Show
		fields = [
			'early_show',
			'early_extra_inf',
			'late_show',
			'late_extra_inf',]
		
class AddWorkshopForm(forms.ModelForm):

	class Meta:
		model = Workshop
		fields = ['title', 'date', 'desc', 'actor',]

class EditWorkshopForm(forms.ModelForm):

	class Meta:
		model = Workshop
		fields = ['title', 'desc', 'actor']

class UpdateAvailabilityForm(forms.ModelForm):
	
	class Meta:
		model = Availability
		fields = ['available']
