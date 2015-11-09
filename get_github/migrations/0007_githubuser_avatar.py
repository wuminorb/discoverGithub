# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_github', '0006_auto_20151109_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='githubuser',
            name='avatar',
            field=models.URLField(null=True),
        ),
    ]
