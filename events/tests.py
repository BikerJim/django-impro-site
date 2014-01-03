from django.test import TestCase

def create_show(show, date, long_desc):
	"""
	A reusable method to create a show object for testing
	"""
	return Show.objects.create(show=show,
        date=date, long_desc=long_desc)
        
