# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 14:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_auto_20170111_1300'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noti', '0025_auto_20170104_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusANotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noti', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.Status')),
                ('who_vote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noti_statusanotification_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
