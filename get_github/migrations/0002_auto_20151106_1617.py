# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('get_github', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='githubrepo',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 6, 8, 16, 43, 510972, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='githubrepo',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='githubrepo',
            name='forks_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='githubrepo',
            name='full_name',
            field=models.TextField(default='undefine'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='githubrepo',
            name='pushed_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 6, 8, 17, 20, 389081, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='githubrepo',
            name='stargazers_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='githubrepo',
            name='watchers_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='githubuser',
            name='blog',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='githubuser',
            name='company',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='githubuser',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 6, 8, 17, 25, 293361, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='githubuser',
            name='emile',
            field=models.EmailField(null=True, max_length=254),
        ),
        migrations.AddField(
            model_name='githubuser',
            name='hireable',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='githubuser',
            name='location',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='githubuser',
            name='login',
            field=models.TextField(default='undefine'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='githubuser',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='githubuser',
            name='public_repo_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='githubuser',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 6, 8, 17, 52, 627925, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
