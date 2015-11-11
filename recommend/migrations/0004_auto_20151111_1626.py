# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0003_auto_20151111_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alsolikerepo',
            name='base_repo',
            field=models.OneToOneField(related_name='also_likes', to='cache_github.GithubRepo'),
        ),
        migrations.AlterField(
            model_name='alsolikerepo',
            name='like_repo',
            field=models.OneToOneField(to='cache_github.GithubRepo'),
        ),
        migrations.AddField(
            model_name='alsolikerepo',
            name='id',
            field=models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, default='1', serialize=False),
            preserve_default=False,
        ),
    ]
