# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache_github', '0008_auto_20151111_1008'),
        ('recommend', '0002_auto_20151111_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alsolikerepo',
            old_name='also_likes',
            new_name='like_repo',
        ),
        migrations.RemoveField(
            model_name='alsolikerepo',
            name='repo',
        ),
        migrations.AddField(
            model_name='alsolikerepo',
            name='base_repo',
            field=models.OneToOneField(default=None, primary_key=True, related_name='also_likes', to='cache_github.GithubRepo'),
            preserve_default=False,
        ),
    ]
