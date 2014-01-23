from django.contrib import admin
from .models import Course
from .models import Student
from .models import Location

class CourseAdmin(admin.ModelAdmin):
	list_display = ('title','teacher','start_date','places_left','show_date')
	list_filter = ('start_date','teacher')
	
class StudentAdmin(admin.ModelAdmin):
	list_display = ('name','course','paid')
	list_filter = ('course','paid')
	list_editable = ('paid',)
	
class LocationAdmin(admin.ModelAdmin):
	list_display = ('title', 'address')
	
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Location, LocationAdmin)
