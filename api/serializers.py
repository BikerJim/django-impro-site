from rest_framework import serializers

from events.models import Show

class EventSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Show
		depth = 1
		fields = ('date','early_show','early_extra_inf','late_show','late_extra_inf')
