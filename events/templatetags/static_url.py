from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def static_url(value):
	"""Searches for {{ STATIC_URL }} and replaces it with the STATIC_URL from settings.py"""
	return value.replace('{{ STATIC_URL }}', settings.STATIC_URL)
static_url.is_safe = True
