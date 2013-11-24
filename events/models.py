from django.db import models


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

class Format(models.Model):
	"""
	A model to hold all the different formats: Title,
	generic explanation, an icon of specific size, min actors,
	max actors. 
	"""
	title = models.CharField(max_length=15)
	description = models.TextField(max_length=250)
	icon = models.ImageField(upload_to="../media/images/")
	min_actors = models.PositiveIntegerField()
	max_actors = models.PositiveIntegerField()
	
	def __unicode__(self):
		return self.title
