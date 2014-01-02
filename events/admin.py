from django.contrib import admin
from .models import Event_date, Format, Show, Workshop
from .models import Availability


class Event_dateAdmin(admin.ModelAdmin):
	list_display = ('pk', '__unicode__', 'event_type', 'taken')

class FormatAdmin(admin.ModelAdmin):
	pass

class ShowAdmin(admin.ModelAdmin):
	list_display = ('pk', 'date', '__unicode__')

class WorkshopAdmin(admin.ModelAdmin):
	list_display = ('date', '__unicode__')

class AvailabilityAdmin(admin.ModelAdmin):
	list_display = ('date', '__unicode__','available')

admin.site.register(Event_date, Event_dateAdmin)
admin.site.register(Format, FormatAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Availability, AvailabilityAdmin)
