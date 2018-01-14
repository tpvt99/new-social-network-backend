# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-27 02:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MomentComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('moment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moment_momentcomment_moment', to='moment.Moment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moment_momentcomment_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('been_vote', models.BooleanField(default=False)),
                ('moment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moment_vote_moment', to='moment.Moment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='moment_vote_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('user', 'moment')]),
        ),
    ]
