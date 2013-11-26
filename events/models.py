from django.db import models
import os
from events.storage import OverwriteStorage

class Event_date(models.Model):
	"""
	A model to hold all the dates which will be related to Shows,
	Workshops, Corporates and Promos etc, basically to populate
	a drop down for the other models
	"""
	EVENT_TYPES = (
		(1, "Early show"),
		(2, "Late show"),
		(3, "Workshop"),
		(4, "Corporate"),
		(5, "Promotion"))
	event_type = models.IntegerField(choices=EVENT_TYPES)
	date = models.DateField()
	
	def __unicode__(self):
		return str(self.date.strftime("%B %d, %Y"))

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
	title = models.CharField(max_length=15)
	description = models.TextField(max_length=250)
	icon = models.ImageField(max_length=1024,storage=OverwriteStorage(), upload_to=image_file_name)
	min_actors = models.PositiveIntegerField()
	max_actors = models.PositiveIntegerField()
	
	def __unicode__(self):
		return self.title
