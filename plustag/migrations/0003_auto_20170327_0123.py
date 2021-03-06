# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-27 01:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moment', '0001_initial'),
        ('plustag', '0002_auto_20170327_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='plustaglife',
            name='moment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plustag_plustaglife_moment', to='moment.Moment'),
        ),
        migrations.AlterField(
            model_name='plustaglife',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plustag_plustaglife_status', to='status.Status'),
        ),
    ]
