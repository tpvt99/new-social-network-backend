# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 15:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0004_auto_20160903_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityEnjoy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.Activity')),
                ('paricipants', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
