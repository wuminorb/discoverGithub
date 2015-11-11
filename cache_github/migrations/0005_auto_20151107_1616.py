# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache_github', '0004_auto_20151107_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='githubuser',
            name='create_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='githubuser',
            name='update_at',
            field=models.DateTimeField(null=True),
        ),
    ]
