# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-21 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0016_auto_20161221_1138'),
        ('noti', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activityparticipants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.ActivityParticipants')),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
    ]
