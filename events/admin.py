from django.contrib import admin
from .models import Event_date

# Register your models here.


class Event_dateAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'event_type')
	
admin.site.register(Event_date, Event_dateAdmin)
