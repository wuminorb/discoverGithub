# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache_github', '0008_auto_20151111_1008'),
        ('recommend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alsolikerepo',
            name='also_likes',
        ),
        migrations.AddField(
            model_name='alsolikerepo',
            name='also_likes',
            field=models.OneToOneField(primary_key=True, to='cache_github.GithubRepo', serialize=False, default='wuminorb/fastjson'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alsolikerepo',
            name='repo',
            field=models.OneToOneField(related_name='also_like', primary_key=True, to='cache_github.GithubRepo', serialize=False),
        ),
    ]
