# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_github', '0005_auto_20151107_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='githubuser',
            name='followers_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='githubuser',
            name='following_count',
            field=models.IntegerField(default=0),
        ),
    ]
