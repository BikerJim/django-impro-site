from django.contrib import admin
from .models import Event_date, Format, Show, Workshop

class Event_dateAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'event_type')

class FormatAdmin(admin.ModelAdmin):
	pass

class ShowAdmin(admin.ModelAdmin):
	list_display = ('date', '__unicode__')

class WorkshopAdmin(admin.ModelAdmin):
	list_display = ('date', '__unicode__')

admin.site.register(Event_date, Event_dateAdmin)
admin.site.register(Format, FormatAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Workshop, WorkshopAdmin)
