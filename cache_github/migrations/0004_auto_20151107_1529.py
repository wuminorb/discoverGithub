# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache_github', '0003_auto_20151106_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='githubrepo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='githubuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='githubrepo',
            name='full_name',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='githubuser',
            name='login',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
