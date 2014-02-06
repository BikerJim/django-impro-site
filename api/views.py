from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from events.models import Show
from api.serializers import EventSerializer

from datetime import date, time, datetime

@api_view(['GET',])
def next_show(request):
	"""
	Spit out the next show after today's date
	"""
	if request.method == 'GET':
		try:
			next_show = Show.objects.filter(date__event_type=1).\
			filter(date__date__gte=datetime.today()).earliest('date')
			serializer = EventSerializer(next_show)
			return Response(serializer.data)
		except Show.DoesNotExist:
			return False
	else:
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
