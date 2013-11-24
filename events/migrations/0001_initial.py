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
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'events', ['Event_date'])

        # Adding model 'Format'
        db.create_table(u'events_format', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=250)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('min_actors', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('max_actors', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'events', ['Format'])


    def backwards(self, orm):
        # Deleting model 'Event_date'
        db.delete_table(u'events_event_date')

        # Deleting model 'Format'
        db.delete_table(u'events_format')


    models = {
        u'events.event_date': {
            'Meta': {'object_name': 'Event_date'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'event_type': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'events.format': {
            'Meta': {'object_name': 'Format'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_actors': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'min_actors': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['events']