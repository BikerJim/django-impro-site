from django import forms
from django.forms import ModelForm

from .models import Course, Student

class CourseSignupForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = [
			'status',
			'course',
			'name',
			'email_address',
			'telephone',
			'heard_about',
			]
