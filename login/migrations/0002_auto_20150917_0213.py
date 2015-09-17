# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_File_Table',
            fields=[
                ('fileid', models.AutoField(serialize=False, primary_key=True)),
                ('userid', models.IntegerField(null=True, blank=True)),
                ('projectid', models.IntegerField(null=True, blank=True)),
                ('user_file_id', models.IntegerField(null=True, blank=True)),
                ('admin_file_path', models.CharField(max_length=512, null=True, blank=True)),
                ('file_status', models.CharField(max_length=512, null=True, blank=True)),
                ('upload_date', models.DateField(null=True, blank=True)),
                ('admin_comments', models.CharField(max_length=512, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cost_Table',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('cost_type', models.CharField(max_length=512, null=True, blank=True)),
                ('file_type', models.CharField(max_length=512, null=True, blank=True)),
                ('cost_per_unit', models.CharField(max_length=512, null=True, blank=True)),
                ('unit_size', models.CharField(max_length=512, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Credit_Table',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('userid', models.IntegerField(null=True, blank=True)),
                ('credit_type', models.CharField(max_length=512, null=True, blank=True)),
                ('credit_amount', models.CharField(max_length=512, null=True, blank=True)),
                ('status', models.CharField(max_length=512, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing_Table',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('userid', models.IntegerField(null=True, blank=True)),
                ('payee_name', models.CharField(max_length=512, null=True, blank=True)),
                ('payee_email', models.CharField(max_length=512, null=True, blank=True)),
                ('payee_details', models.CharField(max_length=512, null=True, blank=True)),
                ('status', models.CharField(max_length=512, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project_Table',
            fields=[
                ('projectid', models.AutoField(serialize=False, primary_key=True)),
                ('userid', models.IntegerField(null=True, blank=True)),
                ('project_title', models.CharField(max_length=512, null=True, blank=True)),
                ('project_instructions', models.CharField(max_length=512, null=True, blank=True)),
                ('project_status', models.CharField(max_length=512, null=True, blank=True)),
                ('admin_comments', models.CharField(max_length=512, null=True, blank=True)),
                ('project_cost', models.CharField(max_length=512, null=True, blank=True)),
                ('pricing_detail_id', models.CharField(max_length=512, null=True, blank=True)),
                ('order_no', models.CharField(max_length=512, null=True, blank=True)),
                ('project_feedback', models.CharField(max_length=512, null=True, blank=True)),
                ('satisfaction_rating', models.CharField(max_length=512, null=True, blank=True)),
                ('material_rating', models.CharField(max_length=512, null=True, blank=True)),
                ('visual_effect_rating', models.CharField(max_length=512, null=True, blank=True)),
                ('storyline_rating', models.CharField(max_length=512, null=True, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Referal_Table',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('userid', models.IntegerField(null=True, blank=True)),
                ('referal_url', models.CharField(max_length=512, null=True, blank=True)),
                ('succesful_referals', models.CharField(max_length=512, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_File_Table',
            fields=[
                ('fileid', models.AutoField(serialize=False, primary_key=True)),
                ('userid', models.IntegerField(null=True, blank=True)),
                ('projectid', models.IntegerField(null=True, blank=True)),
                ('file_type', models.CharField(max_length=512, null=True, blank=True)),
                ('file_title', models.CharField(max_length=512, null=True, blank=True)),
                ('file_web_path', models.CharField(max_length=512, null=True, blank=True)),
                ('file_server_path', models.CharField(max_length=512, null=True, blank=True)),
                ('file_source_type', models.CharField(max_length=512, null=True, blank=True)),
                ('file_status', models.CharField(max_length=512, null=True, blank=True)),
                ('file_upload_date', models.DateField(null=True, blank=True)),
                ('admin_comments', models.CharField(max_length=512, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='user_details',
            name='active_status',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='country',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='dropbox_id',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='facebook_id',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='fb_img_url',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='google_acc_img',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='google_id',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='interests',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='referal_id',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='signup_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='signup_type',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
