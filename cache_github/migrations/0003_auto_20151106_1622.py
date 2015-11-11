# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache_github', '0002_auto_20151106_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='githubrepo',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='githubuser',
            name='company',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='githubuser',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='githubuser',
            name='login',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='githubuser',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
