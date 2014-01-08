from django.shortcuts import render
import django_tables2 as tables
from .models import Availability
from .models import Show
from .models import Event_date
from .models import Workshop

from django_tables2 import RequestConfig
from django.utils.safestring import mark_safe
from django.utils.html import escape

def get_table_data():
	table_row = {}
	table_data = []
	date_list = Event_date.objects.select_related().all()
	avail = Availability.objects.select_related().values('id','date','date__date','date__event_type','available','person__first_name')
	show_list = Show.objects.select_related().values('id','date','late_show__title')
	workshop_list = Workshop.objects.select_related().values('id','date','actor__first_name')
	for date in date_list:
		av = avail.filter(date=date)
		table_row = {}
		for item in av:
			table_row['Date'] = date
			show = [x for x in show_list if x['date']==item['date']]
			workshop = [x for x in workshop_list if x['date']==item['date']]
			if item['date__event_type'] == 1 and show == []:
				table_row['Description'] = "Add show"
			elif item['date__event_type'] == 1 and show != []:
				table_row['Description'] =  show
			elif item['date__event_type'] == 2 and workshop == []:
				table_row['Description'] =  "Add workshop"
			elif item['date__event_type'] == 2 and workshop != []:
				table_row['Description'] =  workshop
			table_row[item['person__first_name']] = item['available']
			table_row['show_id'] = item['id']
		table_data.append(table_row)
	return table_data

class ShoverviewTable(tables.Table):		
	Date = tables.Column()
	Description = tables.Column()
	Peter = tables.BooleanColumn()
	Sarah = tables.BooleanColumn()
	Ben = tables.BooleanColumn()
	Jim = tables.BooleanColumn()
	Janette = tables.BooleanColumn()
	Ashley = tables.BooleanColumn()
	Trista = tables.BooleanColumn()
	Luke = tables.BooleanColumn()
	Jochem = tables.BooleanColumn()
	Anne = tables.BooleanColumn()
	Jake = tables.BooleanColumn()
	
	def render_Description(self, value, record):
		if value != 'Add show' and record['Date'].event_type == 1:
			show_id = value[0]['id']
			show_desc = value[0]['late_show__title']
			show_url = mark_safe('<a href="/events/shows/edit/{0}/">{1}</a>'\
			.format(escape(show_id), escape(show_desc)))
		elif value != 'Add workshop' and record['Date'].event_type == 2:
			show_id = value[0]['id']
			show_desc = value[0]['actor__first_name']
			show_url = mark_safe('<a href="/events/workshops/edit/{0}/">{1}</a>'\
			.format(escape(show_id), escape(show_desc)))
		elif value == 'Add show' and record['Date'].event_type == 1:
			show_url = mark_safe('<a href="/events/shows/add/">{0}</a>'\
			.format(escape(value)))
		elif value == 'Add workshop' and record['Date'].event_type == 2:
			show_url = mark_safe('<a href="/events/workshops/add/">{0}</a>'\
			.format("Add Workshop"))
		else:
			show_url = ''
		return show_url

	class Meta:
		# add class="paleblue" to <table> tag
		attrs = {"class": "paleblue"}

def shoverview(request):
	table = ShoverviewTable(get_table_data())
	RequestConfig(request).configure(table)
	return render(request, 'events/shoverview.html', {
					'table': table,
						})
