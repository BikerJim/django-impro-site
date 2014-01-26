from django.db import models
from django.core.urlresolvers import reverse

from datetime import timedelta
from datetime import date

from django.contrib.auth.models import User
from events.models import Event_date

class Location(models.Model):
	title 				= models.CharField(max_length=50, verbose_name=u'Location Title')
	address 			= models.CharField(max_length=500, verbose_name=u'Address')
	telephone 			= models.CharField(max_length=50, verbose_name=u'Location\'s telephone number', blank=True)
	map_url 			= models.TextField(max_length=500, verbose_name=u'google map URL')
	public_transport 	= models.TextField(max_length=500, verbose_name=u'Public Transport Access', blank=True)
	by_car 				= models.TextField(max_length=500, verbose_name=u'Access by car', blank=True)
	
	def __unicode__(self):
		return self.title

class Course(models.Model):
	title 		= models.CharField(max_length=255)
	description = models.TextField(verbose_name=u'Course Description', max_length=200)
	start_date 	= models.DateField()
	end_date	= models.DateField()
	duration 	= models.IntegerField(verbose_name=u'Number of weeks')
	start_time	= models.TimeField(verbose_name=u'Start Time')
	end_time	= models.TimeField(verbose_name=u'End Time')
	show_date 	= models.ForeignKey(Event_date, limit_choices_to={'event_type':1}, related_name='early_show')
	teacher 	= models.ForeignKey(User, limit_choices_to={'groups__name':'crew'})
	location 	= models.ForeignKey(Location)
	cost 		= models.IntegerField()
	places_left	= models.IntegerField()
	
	def __unicode__(self):
		return self.title
		
class Student(models.Model):
	STATUS_CHOICES	= (
					(1, 'Reserved'),
					(2, 'Paid'),
					(3, 'Waiting list'),
					)
	date_registered = models.DateTimeField(auto_now_add=True, null=True)
	name 			= models.CharField(max_length=30)
	email_address 	= models.EmailField(verbose_name=u'email address')
	telephone 		= models.CharField(
						max_length=20,
						verbose_name=u'Contact telephone number',
						help_text=u'in emergencies its useful to be able to contact people quickly',
						blank=True)
	course  		= models.ForeignKey(Course, verbose_name=u'Course')
	status			= models.IntegerField(choices=STATUS_CHOICES, default=1)
#	paid			= models.BooleanField(verbose_name=u'Payment Status')
	heard_about 	= models.CharField(
						max_length=250,
						verbose_name=u'How Did You Hear About Us',
						help_text=u"We'd really like to know how you heard about easylaughs!")
	
#	def get_absolute_url(self):
#		return reverse('course_reservation_thanks')
	
	def save(self, *args, **kwargs):
		if self.status == 1:
			course = Course.objects.get(pk=self.course.id)
			if course.places_left > 0:
				course.places_left -= 1
				course.save()
		super(Student, self).save(*args, **kwargs)
				
