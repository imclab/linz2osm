# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WorksliceFeature.dirty'
        db.add_column('workslices_workslicefeature', 'dirty',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WorksliceFeature.dirty'
        db.delete_column('workslices_workslicefeature', 'dirty')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'data_dict.dataset': {
            'Meta': {'object_name': 'Dataset'},
            'database_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data_dict.Group']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'primary_key': 'True'}),
            'srid': ('django.db.models.fields.IntegerField', [], {}),
            'update_method': ('django.db.models.fields.CharField', [], {'default': "'manual'", 'max_length': '255'}),
            'version': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'data_dict.group': {
            'Meta': {'object_name': 'Group'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'primary_key': 'True'})
        },
        'data_dict.layer': {
            'Meta': {'object_name': 'Layer'},
            'datasets': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data_dict.Dataset']", 'through': "orm['data_dict.LayerInDataset']", 'symmetrical': 'False'}),
            'entity': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'geometry_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data_dict.Group']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pkey_name': ('django.db.models.fields.CharField', [], {'default': "'ogc_fid'", 'max_length': '255'}),
            'processors': ('linz2osm.utils.db_fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'special_dataset_name_tag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'special_dataset_version_tag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'special_end_node_field_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'special_node_reuse_logic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'special_node_tag_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'special_start_node_field_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tags_ql': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wfs_cql_filter': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'wfs_type_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'data_dict.layerindataset': {
            'Meta': {'object_name': 'LayerInDataset'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dataset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data_dict.Dataset']"}),
            'extent': ('django.contrib.gis.db.models.fields.GeometryField', [], {'null': 'True'}),
            'features_total': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data_dict.Layer']"}),
            'tagging_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'workslices.workslice': {
            'Meta': {'object_name': 'Workslice'},
            'checked_out_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'checkout_extent': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'feature_count': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'followup_deadline': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layer_in_dataset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data_dict.LayerInDataset']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'status_changed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'workslices.workslicefeature': {
            'Meta': {'object_name': 'WorksliceFeature'},
            'dirty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'feature_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layer_in_dataset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data_dict.LayerInDataset']"}),
            'workslice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workslices.Workslice']"})
        }
    }

    complete_apps = ['workslices']