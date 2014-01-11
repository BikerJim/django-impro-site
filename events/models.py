from django.db import models
import os
from django.core.files.storage import default_storage as storage
#from events.storage import OverwriteStorage
from django.contrib.auth.models import User
from django.db.models import Q
from PIL import Image
_imaging = Image.core

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
		(1, "Show"),
		(2, "Workshop"),
		(3, "Rehearsal"),
		(4, "Corporate"),
		(5, "Promotion"),
		)
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
	icon = models.ImageField(max_length=1024, upload_to=image_file_name)
	min_actors = models.PositiveIntegerField()
	max_actors = models.PositiveIntegerField()

	def save(self, *args, **kwargs):
#		if not self.id and not self.icon:
#			return
		super(Format, self).save(*args, **kwargs)
		image = Image.open(self.icon)
		(width,height) = image.size

		if (150 / width < 150 / height):
			factor = 150.00/height
		else:
			factor = 150.00/width
			
		size= (int(width*factor),int(height*factor))
		image = image.resize(size, Image.ANTIALIAS)
		fh = storage.open(self.icon.name, "w")
		format = 'png'
		image.save(fh, format)
		fh.close()

	def __unicode__(self):
		return self.title

class Show(models.Model):
	"""
	A model to hold the shows, taking a format on an event_date
	"""
	date = models.OneToOneField(Event_date, 
				limit_choices_to=Q(date__gte=datetime.today()) & Q(event_type=1) & Q(taken=False),
				related_name='showdate')
	early_show = models.ForeignKey(Format, related_name='early_show', null=True, blank=True)
	early_extra_inf = models.TextField(max_length=500, blank=True)
	late_show = models.ForeignKey(Format, related_name='late_show')
	late_extra_inf = models.TextField(max_length=500, blank=True)

	def __unicode__(self):
		return self.late_show.title

class Workshop(models.Model):
	"""
	A model to hold the workshops, taking a title, description
	and an event_date
	"""
	title = models.CharField(max_length=50)
	date = models.OneToOneField(Event_date,
				limit_choices_to=Q(date__gte=datetime.today()) & Q(event_type=2) & Q(taken=False),
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
	cast = models.BooleanField(default=False)
	host = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.person.first_name
		
	class Meta:
		verbose_name_plural = "Availability"
	
