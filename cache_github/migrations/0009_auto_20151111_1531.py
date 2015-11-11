# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache_github', '0008_auto_20151111_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='githubrepo',
            name='stargazers',
            field=models.ManyToManyField(to='cache_github.GithubUser', related_name='starred'),
        ),
    ]
