# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-03 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loma', '0009_auto_20190203_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loma_attendance_model',
            name='loma_attendance',
            field=models.CharField(choices=[('A', 'A'), ('P', 'P')], default='A', max_length=120),
        ),
    ]