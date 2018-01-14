# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0016_activitycomment_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='share',
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_code',
            field=models.CharField(choices=[('sport', 'sport'), ('birth', 'birthday'), ('school', 'school'), ('outgoing', 'outgoing'), ('help', 'help')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='who_join',
            field=models.CharField(choices=[('me', 'me'), ('fr', 'friend'), ('frfr', 'friendoffriend'), ('world', 'world')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='who_share',
            field=models.CharField(choices=[('me', 'onlyme'), ('invite', 'invite'), ('fr', 'friends'), ('frfr', 'friendoffriend'), ('world', 'world')], max_length=10, null=True),
        ),
    ]