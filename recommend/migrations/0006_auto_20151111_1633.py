# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache_github', '0009_auto_20151111_1531'),
        ('recommend', '0005_auto_20151111_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alsolikerepo',
            name='base_repo',
        ),
        migrations.AddField(
            model_name='alsolikerepo',
            name='base_repo',
            field=models.OneToOneField(related_name='also_likes', default=None, to='cache_github.GithubRepo'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='alsolikerepo',
            name='like_repo',
        ),
        migrations.AddField(
            model_name='alsolikerepo',
            name='like_repo',
            field=models.OneToOneField(default=None, to='cache_github.GithubRepo'),
            preserve_default=False,
        ),
    ]
