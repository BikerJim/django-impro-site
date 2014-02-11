from django.contrib import admin
from .models import Course
from .models import Student
from .models import Location

class CourseAdmin(admin.ModelAdmin):
	list_display = ('title','teacher','start_date','places_left','show_date',)
	list_filter = ('start_date','teacher',)
	
class StudentAdmin(admin.ModelAdmin):
	list_display = ('name','email_address','course','ebird_disc','to_pay','total_paid','status','date_registered',)
	list_filter = ('course','status',)
	list_editable = ('total_paid',)
	
class LocationAdmin(admin.ModelAdmin):
	list_display = ('title', 'address',)
	
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Location, LocationAdmin)
