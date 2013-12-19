from django import forms
from django.forms import ModelForm

from events.models import Show

class AddShowForm(forms.ModelForm):

	class Meta:
		model = Show

class EditShowForm(forms.ModelForm):

	class Meta:
		model = Show
