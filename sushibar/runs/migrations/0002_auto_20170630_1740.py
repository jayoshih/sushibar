# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 17:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('runs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='contentchannel',
            name='followers',
            field=models.ManyToManyField(related_name='saved_channels', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='channelrunstage',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='runs.ContentChannelRun'),
        ),
    ]
