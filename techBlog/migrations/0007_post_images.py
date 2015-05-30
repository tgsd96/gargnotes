# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techBlog', '0006_auto_20150415_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
