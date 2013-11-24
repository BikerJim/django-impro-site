# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event_date'
        db.create_table(u'events_event_date', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_type', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'events', ['Event_date'])


    def backwards(self, orm):
        # Deleting model 'Event_date'
        db.delete_table(u'events_event_date')


    models = {
        u'events.event_date': {
            'Meta': {'object_name': 'Event_date'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'event_type': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['events']