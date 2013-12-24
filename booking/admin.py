from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'reserved_by', 'number_of_tickets', 'early_show', 'late_show', 'heard_about')

admin.site.register(Reservation, ReservationAdmin)
