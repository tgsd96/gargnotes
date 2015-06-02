# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techBlog', '0008_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publisher',
            field=models.CharField(default=b'Tushar Garg', max_length=255),
            preserve_default=True,
        ),
    ]
