from django.test import TestCase

import datetime
from django.utils import timezone

from django.core.urlresolvers import reverse

from .models import Show

def create_show(show, date, long_desc):
	"""
	A reusable method to create a show object for testing
	"""
	return Show.objects.create(show=show,
        date=date, long_desc=long_desc)
        
class IndexViewTests(TestCase):
	def test_index_with_no_shows(self):
		"""
		if no Shows exist it should show a message 'No Shows planned'
		"""
		response = self.client.get(reverse('events:index'))
		
