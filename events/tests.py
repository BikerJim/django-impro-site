from django.test import TestCase

import datetime
from django.utils import timezone

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Show, Workshop, Format, Event_date

def create_event(event_type, title, days, **kwargs):
	"""
	A reusable method to create a show object for testing
	"""
	date = Event_date.objects.create(
		event_type = event_type,
		date = timezone.now() + datetime.timedelta(days=days),
		taken = False,
		)
	
	long_desc = "Test Show's long description"

	if event_type == 1 or event_type == 2:
		show = Format.objects.create(
			title=title,
			short_desc = "test format short desc",
			icon = "/gfx/testformat.jpg",
			min_actors = 0,
			max_actors = 2,
		)
		return Show.objects.create(show=show,date=date, long_desc=long_desc)
	elif event_type == 3:
		desc="Test Workshop description."
		actor = User.objects.create(
			username = kwargs['username'],
			email = "testactor@tests.com",
		)
		return Workshop.objects.create(title=title, date=date, desc=desc, actor=actor)

class IndexViewTests(TestCase):
	def test_index_with_no_shows(self):
		"""
		if no Shows exist it should show a message 'No Shows planned'
		"""
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Nothing to see here.")
		self.assertQuerysetEqual(response.context['early'], [])
		self.assertQuerysetEqual(response.context['late'], [])
		self.assertQuerysetEqual(response.context['workshop'], [])

	def test_index_with_future_workshop(self):
		"""
		One workshop in the future
		"""
		event=create_event(3, "Test Workshop", 5, username='user1')
		response = self.client.get(reverse('index'))
		self.assertEqual(response.context['workshop'], event)

	def test_index_with_past_workshop(self):
		"""
		One workshop in the past
		"""
		event=create_event(3, "Test Workshop", -5, username='user1')
		response = self.client.get(reverse('index'))
		self.assertQuerysetEqual(response.context['workshop'], [])

	def test_index_with_past_workshop_and_future_workshop(self):
		"""
		One workshop in the past, and one in the future
		"""
		eventpast=create_event(3, "Test Past Workshop", -5, username='user1')
		eventfuture=create_event(3, "Test Future Workshop", 5, username="user2")
		response = self.client.get(reverse('index'))
		self.assertEqual(response.context['workshop'], eventfuture)

	def test_index_with_future_early_show(self):
		"""
		One early show in the future
		"""
		event=create_event(1, "Early Show", 5)
		response = self.client.get(reverse('index'))
		self.assertQuerysetEqual(response.context['late'], [])
		self.assertEqual(response.context['early'], event)

	def test_index_with_future_late_show(self):
		"""
		One early show in the future
		"""
		event=create_event(2, "Late Show", 5)
		response = self.client.get(reverse('index'))
		self.assertQuerysetEqual(response.context['early'], [])
		self.assertEqual(response.context['late'], event)
		
	def test_index_with_future_late_and_early_show(self):
		"""
		One early, one late show in the future
		"""
		event1=create_event(1, "Early Show", 5)
		event2=create_event(2, "Late Show", 5)
		response = self.client.get(reverse('index'))
		self.assertEqual(response.context['early'], event1)
		self.assertEqual(response.context['late'], event2)		

	def test_index_with_future_late_and_past_early_show(self):
		"""
		One early, one late show in the future
		"""
		event1=create_event(1, "Early Show", -5)
		event2=create_event(2, "Late Show", 5)
		response = self.client.get(reverse('index'))
		self.assertQuerysetEqual(response.context['early'], [])
		self.assertEqual(response.context['late'], event2)		

	def test_index_with_future_early_and_past_late_show(self):
		"""
		One early, one late show in the future
		"""
		event1=create_event(1, "Early Show", 5)
		event2=create_event(2, "Late Show", -5)
		response = self.client.get(reverse('index'))
		self.assertQuerysetEqual(response.context['late'], [])
		self.assertEqual(response.context['early'], event1)
		
	def test_index_with_future_late_and_later_early_show(self):
		"""
		One early, one late show in the future
		"""
		event1=create_event(1, "Early Show", 10)
		event2=create_event(2, "Late Show", 5)
		response = self.client.get(reverse('index'))
		self.assertQuerysetEqual(response.context['early'], [])
		self.assertEqual(response.context['late'], event2)

	def test_index_with_future_early_and_later_late_show(self):
		"""
		One early, one late show in the future
		"""
		event1=create_event(1, "Early Show", 5)
		event2=create_event(2, "Late Show", 10)
		response = self.client.get(reverse('index'))
		self.assertQuerysetEqual(response.context['late'], [])
		self.assertTrue(response.context['early'], event1)
