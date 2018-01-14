# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0027_auto_20170115_1505'),
        ('activities', '0061_auto_20170115_1440'),
        ('noti', '0030_auto_20170112_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitiesANotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activitiespost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.ActivitiesPost')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
                ('noti', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
    ]
