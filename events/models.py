from django.db import models
import os
from events.storage import OverwriteStorage
from django.contrib.auth.models import User
from django.db.models import Q

from datetime import date, time, datetime

def image_file_name(instance, filename):
	"""
	This function takes an uploaded filename, takes the extension.
	Then it rebuilds the entire path from the MEDIA_ROOT up, by
	renaming the file to the title of the instance that called it, after stripping
	out the spaces, and putting the extension back on, then
	puts it into the specified folder 
	"""
	ext = filename[-4:]
	new_filename = os.path.join('images',str(instance.image_folder),str(instance.title).replace(" ","").lower()+ext)
	return new_filename

class Event_date(models.Model):
	"""
	A model to hold all the dates which will be related to Shows,
	Workshops, Corporates and Promos etc, basically to populate
	a drop down for the other models
	"""
	EVENT_TYPES = (
		(1, "8 o'clock show"),
		(2, "9 o'clock show"),
		(3, "Workshop"),
		(4, "Rehearsal"),
		(5, "Corporate"),
		(6, "Promotion"))
	event_type = models.IntegerField(choices=EVENT_TYPES)
	date = models.DateField()
	taken = models.BooleanField(default=False)
	class Meta:
		ordering = ['date']
		unique_together = ("date", "event_type")
	def __unicode__(self):
		return "{0}, {1}".format(str(self.date.strftime("%B %d, %Y")),str(self.EVENT_TYPES[self.event_type-1][1]))

class Format(models.Model):
	"""
	A model to hold all the different formats: Title,
	generic explanation, an icon of specific size, min actors,
	max actors. 
	"""
	image_folder = "formats"
	title = models.CharField(max_length=50)
	short_desc = models.TextField(max_length=150)
	icon = models.ImageField(max_length=1024,storage=OverwriteStorage(), upload_to=image_file_name)
	min_actors = models.PositiveIntegerField()
	max_actors = models.PositiveIntegerField()
	
	def __unicode__(self):
		return self.title

class Show(models.Model):
	"""
	A model to hold the shows, taking a format on an event_date
	"""
	show = models.ForeignKey(Format, related_name='showtitle')
	date = models.OneToOneField(Event_date, 
				limit_choices_to=Q(date__gte=datetime.today()) & (Q(event_type=1) | Q(event_type=2)) & Q(taken=False),
				related_name='showdate')
	long_desc = models.TextField(max_length=500, blank=True)

	def __unicode__(self):
		return self.show.title
		
class Workshop(models.Model):
	"""
	A model to hold the workshops, taking a title, description
	and an event_date
	"""
	title = models.CharField(max_length=50)
	date = models.OneToOneField(Event_date,
				limit_choices_to=Q(date__gte=datetime.today()) & Q(event_type=3) & Q(taken=False),
				related_name='workshopdate')
	desc = models.TextField(max_length=500, blank=True)
	actor = models.ForeignKey(User, limit_choices_to={'groups__name':'actor'})
			
	def __unicode__(self):
		return self.title

class Availability(models.Model):
	"""
	A model to hold the availability of the Crew 
	(actors, tech, door, musician)
	It will have different lists of users (by group 'crew'), 
	list of dates (after today, relevant to group)
	Availability boolean (yes,no,maybe?)
	"""
	date = models.ForeignKey(Event_date)
	person = models.ForeignKey(User, limit_choices_to={'groups__name':'crew'})
	available = models.NullBooleanField(default=False)
	def __unicode__(self):
		return self.person.first_name
		
	class Meta:
		verbose_name_plural = "Availability"
	
