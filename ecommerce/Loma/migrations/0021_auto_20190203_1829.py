# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-03 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loma', '0020_auto_20190203_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approved_pl_by_loma',
            name='cal_offer_price',
            field=models.FloatField(null=True),
        ),
    ]