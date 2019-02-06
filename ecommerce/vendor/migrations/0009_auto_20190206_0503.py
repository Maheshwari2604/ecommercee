# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-05 23:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Loma', '0033_remove_daily_price_list_vendor_id'),
        ('vendor', '0008_auto_20190206_0459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor_master',
            old_name='loma_zone',
            new_name='loma_id',
        ),
        migrations.AddField(
            model_name='vendor_daily_pl',
            name='Mandi_name',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Loma.md'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor_daily_pl',
            name='loma_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Loma.Loma_master'),
            preserve_default=False,
        ),
    ]
