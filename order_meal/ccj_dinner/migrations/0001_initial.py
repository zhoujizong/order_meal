# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-18 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ordered_list',
            fields=[
                ('staff_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='staff_action_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.IntegerField()),
                ('staff_name', models.CharField(max_length=50)),
                ('group_name', models.CharField(max_length=50)),
                ('create_time', models.TimeField(auto_now=True)),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='staff_base_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.IntegerField()),
                ('staff_name', models.CharField(max_length=50)),
                ('group_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['staff_id'],
            },
        ),
    ]