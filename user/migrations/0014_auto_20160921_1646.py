# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20160921_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityonpost',
            name='activity_icon',
            field=models.CharField(choices=[('Sport', (('1', 'active person'), ('2', 'badminton'), ('3', 'ride bike'), ('4', 'climbing'), ('5', 'go fishing'), ('6', 'golf'), ('7', 'horse riding'), ('8', 'flying a kite'), ('9', 'canoe'), ('10', 'swimming'), ('11', 'camping'), ('12', 'running'), ('13', 'skateboard'), ('14', 'ski-lift'), ('15', 'surfer'), ('16', 'walking')))], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='activityonpost',
            name='activity_icon_description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='activityonpost',
            name='activity_name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
