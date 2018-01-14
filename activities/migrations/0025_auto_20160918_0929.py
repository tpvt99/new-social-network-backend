# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 09:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0024_remove_activityparticipants_participants'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoreInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(default=0)),
                ('activityparticipants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities_moreinfo_activityparticipants', to='activities.ActivityParticipants')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities_moreinfo_person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who_being_vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities_vote_who_being_vote', to=settings.AUTH_USER_MODEL)),
                ('who_vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities_vote_who_vote', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activityparticipants',
            name='participants',
            field=models.ManyToManyField(through='activities.MoreInfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('who_being_vote', 'who_vote')]),
        ),
    ]