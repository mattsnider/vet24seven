# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EmailRecorder'
        db.create_table('homepage_emailrecorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_ts', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('modify_ts', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('campaign', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('medium', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('source', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('homepage', ['EmailRecorder'])


    def backwards(self, orm):
        # Deleting model 'EmailRecorder'
        db.delete_table('homepage_emailrecorder')


    models = {
        'homepage.emailrecorder': {
            'Meta': {'object_name': 'EmailRecorder'},
            'campaign': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'create_ts': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'modify_ts': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'source': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['homepage']