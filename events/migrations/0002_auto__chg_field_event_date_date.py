# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Event_date.date'
        db.alter_column(u'events_event_date', 'date', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):

        # Changing field 'Event_date.date'
        db.alter_column(u'events_event_date', 'date', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'events.event_date': {
            'Meta': {'object_name': 'Event_date'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'event_type': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['events']