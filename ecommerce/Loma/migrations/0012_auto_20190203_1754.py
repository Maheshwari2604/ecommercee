# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-03 12:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loma', '0011_auto_20190203_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approved_pl_by_loma',
            name='cal_offer_price',
        ),
        migrations.RemoveField(
            model_name='approved_pl_by_loma',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='approved_pl_by_loma',
            name='verified',
        ),
    ]
