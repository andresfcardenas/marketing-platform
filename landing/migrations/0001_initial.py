# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LandingRegister'
        db.create_table(u'landing_landingregister', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=250)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'landing', ['LandingRegister'])

        # Adding model 'Slogan'
        db.create_table(u'landing_slogan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slogan', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'landing', ['Slogan'])

        # Adding model 'MainImage'
        db.create_table(u'landing_mainimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Description', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'landing', ['MainImage'])

        # Adding model 'Testimonial'
        db.create_table(u'landing_testimonial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200)),
        ))
        db.send_create_signal(u'landing', ['Testimonial'])

        # Adding model 'Function'
        db.create_table(u'landing_function', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200)),
        ))
        db.send_create_signal(u'landing', ['Function'])


    def backwards(self, orm):
        # Deleting model 'LandingRegister'
        db.delete_table(u'landing_landingregister')

        # Deleting model 'Slogan'
        db.delete_table(u'landing_slogan')

        # Deleting model 'MainImage'
        db.delete_table(u'landing_mainimage')

        # Deleting model 'Testimonial'
        db.delete_table(u'landing_testimonial')

        # Deleting model 'Function'
        db.delete_table(u'landing_function')


    models = {
        u'landing.function': {
            'Meta': {'object_name': 'Function'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'landing.landingregister': {
            'Meta': {'object_name': 'LandingRegister'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'landing.mainimage': {
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'MainImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'landing.slogan': {
            'Meta': {'object_name': 'Slogan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'landing.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['landing']