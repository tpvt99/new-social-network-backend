# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0020_auto_20160917_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_icon',
            field=models.CharField(choices=[('Sport', (('1', 'badminton'), ('2', 'surfing'), ('3', 'hiking'), ('4', 'swimming'))), ('None', (('0,', 'no icon'),))], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_code',
            field=models.CharField(choices=[('Sport', (('1', 'swimming'), ('2', 'football'), ('3', 'badminton'), ('4', 'walking'), ('5', ''))), ('Learning', (('100', 'learning'), ('101', 'school'))), ('Party', (('200', 'party'), ('201', 'eat'), ('202', 'date'))), ('Free', (('0', 'create by you'),))], max_length=10, null=True),
        ),
    ]
