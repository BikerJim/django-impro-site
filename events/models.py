from django.db import models
import os
from events.storage import OverwriteStorage
from django.contrib.auth.models import User

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
		(4, "Corporate"),
		(5, "Promotion"))
	event_type = models.IntegerField(choices=EVENT_TYPES)
	date = models.DateField() 
	
	def __unicode__(self):
		return str(self.date.strftime("%B %d, %Y"))+", "+str(self.EVENT_TYPES[self.event_type-1][1])

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
	date = models.OneToOneField(Event_date, related_name='showdate')
	long_desc = models.TextField(max_length=500, blank=True)
			
	def __unicode__(self):
		return self.show.title
		
class Workshop(models.Model):
	"""
	A model to hold the workshops, taking a title, description
	and an event_date
	"""
	title = models.CharField(max_length=50)
	date = models.OneToOneField(Event_date, related_name='workshopdate')
	desc = models.TextField(max_length=500, blank=True)
	actor = models.ForeignKey(User, limit_choices_to={'groups__name':'actor'})
			
	def __unicode__(self):
		return self.title
