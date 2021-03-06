# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-17 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0004_contentchannelrun_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentchannel',
            name='changes_needed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contentchannel',
            name='qa_sheet_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contentchannel',
            name='run_needed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contentchannel',
            name='trello_webhook_id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contentchannel',
            name='trello_webhook_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
