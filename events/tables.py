from django.shortcuts import render
import django_tables2 as tables
from .models import Availability
from .models import Show
from .models import Event_date

from django_tables2 import RequestConfig

def get_table_data():
	table_row = {}
	table_data = []
		
	for date in Event_date.objects.select_related().all():
		av = Availability.objects.select_related().filter(date=date)
		table_row = {}
		for item in av:
			table_row['Date'] = item.date
			table_row['Show'] = Show.objects.select_related().filter(date=item.date)
			table_row['Cast'] = item.cast
			table_row[item.person.first_name] = item.available
		table_data.append(table_row)
	return table_data

class ShoverviewTable(tables.Table):
	Date = tables.Column()
	Show = tables.Column()
	Cast = tables.BooleanColumn()
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
	
	class Meta:
		# add class="paleblue" to <table> tag
		attrs = {"class": "paleblue"}

def shoverview(request):
	table = ShoverviewTable(get_table_data())
	RequestConfig(request).configure(table)
	return render(request, 'events/shoverview.html', {
					'table': table,
						})


