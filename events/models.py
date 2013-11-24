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
