# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-03 12:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20190203_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_price',
            name='price',
        ),
    ]