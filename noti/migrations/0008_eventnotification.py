# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20170101_0840'),
        ('noti', '0007_notification_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
    ]
