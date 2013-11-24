from django.contrib import admin
from .models import Event_date, Format

class Event_dateAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'event_type')

class FormatAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Event_date, Event_dateAdmin)
admin.site.register(Format, FormatAdmin)
