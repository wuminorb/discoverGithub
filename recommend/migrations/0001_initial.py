# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache_github', '0008_auto_20151111_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlsoLikeRepo',
            fields=[
                ('repo', models.OneToOneField(to='cache_github.GithubRepo', primary_key=True, serialize=False)),
                ('weight', models.IntegerField(default=0)),
                ('also_likes', models.ManyToManyField(to='cache_github.GithubRepo', related_name='also_like')),
            ],
        ),
    ]
