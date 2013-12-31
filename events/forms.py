from django import forms
from django.forms import ModelForm

from events.models import Show, Workshop

class AddShowForm(forms.ModelForm):

	class Meta:
		model = Show

class EditShowForm(forms.ModelForm):

	class Meta:
		model = Show
		fields = ['show', 'long_desc']
		
class AddWorkshopForm(forms.ModelForm):

	class Meta:
		model = Workshop

class EditWorkshopForm(forms.ModelForm):

	class Meta:
		model = Workshop
		fields = ['title', 'desc', 'actor']
