# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-24 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccj_dinner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_action_log',
            name='create_time',
            field=models.IntegerField(),
        ),
    ]
