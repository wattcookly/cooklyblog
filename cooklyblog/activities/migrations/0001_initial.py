# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('session_name', models.CharField(max_length=120)),
                ('activity', models.ForeignKey(to='activities.Activity')),
            ],
        ),
    ]
