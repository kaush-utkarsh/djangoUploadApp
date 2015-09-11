# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('userid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=512, null=True, blank=True)),
                ('email', models.CharField(max_length=512, null=True, blank=True)),
                ('username', models.CharField(max_length=512, null=True, blank=True)),
                ('password', models.CharField(max_length=512, null=True, blank=True)),
            ],
        ),
    ]
