# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techBlog', '0002_post_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
