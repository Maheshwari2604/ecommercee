# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-09 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0009_auto_20190206_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_master',
            name='loma_zone',
            field=models.CharField(default=2, max_length=120),
            preserve_default=False,
        ),
    ]
