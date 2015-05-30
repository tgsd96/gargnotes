# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techBlog', '0003_auto_20150405_0443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
    ]
