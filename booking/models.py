from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from events.models import Show, Event_date

from datetime import date

class Reservation(models.Model):
	TICKET_NUMBERS = (
		(1, '1'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5'),
		(6, '6'),
		(7, '7'),
		(8, '8'),
		(9, '9'),
		(10, '10'),
	)
	HEARD_ABOUT = (
		(1, 'Flyer'),
		(2, 'Crea Agenda'),
		(3, 'Last Minute Ticket'),
		(4, 'GroupOn, GroupDeal etc'),
		(5, 'Uitkrant'),
		(6, 'Uit123'),
		(7, 'IAmsterdam'),
		(8, 'web search'),
		(9, 'friends'),
		(10, 'easylaughs student'),
		(11, 'Something else'),
	)
	
	created_date = models.DateTimeField(auto_now_add=True)
	event_date = models.ForeignKey(Event_date)
	reserved_by = models.CharField(max_length=20)
	email_address = models.EmailField(max_length=254)
	number_of_tickets = models.IntegerField(choices=TICKET_NUMBERS)
	early_show = models.BooleanField(default=True)
	late_show = models.BooleanField(default=True)
	promo_code = models.CharField(blank=True,max_length=10)
	heard_about = models.IntegerField(choices=HEARD_ABOUT)
	
	def get_absolute_url(self):
		return reverse('reserve_thanks')
	
	def __unicode__(self):
		return str(self.event_date)
