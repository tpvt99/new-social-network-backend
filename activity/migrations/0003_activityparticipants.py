# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-25 16:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0002_auto_20161125_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityParticipants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_invite', models.BooleanField(default=False)),
                ('guess_invite', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=False)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_activityparticipants_person', to='activity.Activity')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_activityparticipants_person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
