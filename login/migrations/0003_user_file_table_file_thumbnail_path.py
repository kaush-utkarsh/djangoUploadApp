# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20150917_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_file_table',
            name='file_thumbnail_path',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
