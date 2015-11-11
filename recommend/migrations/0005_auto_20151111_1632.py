# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache_github', '0009_auto_20151111_1531'),
        ('recommend', '0004_auto_20151111_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alsolikerepo',
            name='base_repo',
        ),
        migrations.AddField(
            model_name='alsolikerepo',
            name='base_repo',
            field=models.ManyToManyField(to='cache_github.GithubRepo', related_name='also_likes'),
        ),
        migrations.RemoveField(
            model_name='alsolikerepo',
            name='like_repo',
        ),
        migrations.AddField(
            model_name='alsolikerepo',
            name='like_repo',
            field=models.ManyToManyField(to='cache_github.GithubRepo'),
        ),
    ]
