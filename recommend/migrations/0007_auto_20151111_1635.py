# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0006_auto_20151111_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alsolikerepo',
            name='base_repo',
            field=models.ForeignKey(related_name='also_likes', to='cache_github.GithubRepo'),
        ),
        migrations.AlterField(
            model_name='alsolikerepo',
            name='like_repo',
            field=models.ForeignKey(to='cache_github.GithubRepo'),
        ),
    ]
