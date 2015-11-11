# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache_github', '0007_githubuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='githubrepo',
            name='stargazers',
            field=models.ManyToManyField(to='cache_github.GithubUser'),
        ),
        migrations.AlterField(
            model_name='githubrepo',
            name='create_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='githubrepo',
            name='pushed_at',
            field=models.DateTimeField(null=True),
        ),
    ]
