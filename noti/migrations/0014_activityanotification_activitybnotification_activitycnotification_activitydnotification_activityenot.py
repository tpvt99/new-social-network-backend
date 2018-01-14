# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 02:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0017_auto_20170102_0152'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noti', '0013_eventinotification'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityANotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('activityparticipants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.ActivityParticipants')),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityBNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('activityparticipants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.ActivityParticipants')),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityCNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityDNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
                ('guess', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noti_activitydnotification_guess', to=settings.AUTH_USER_MODEL)),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityENotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('activityparticipants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.ActivityParticipants')),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityFNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('activityparticipants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.ActivityParticipants')),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityGNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityHNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
                ('guess', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noti_activityhnotification_guess', to=settings.AUTH_USER_MODEL)),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityINotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
    ]
