# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]
