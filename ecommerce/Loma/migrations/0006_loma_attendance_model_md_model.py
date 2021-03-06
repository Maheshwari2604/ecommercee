# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-03 10:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_vendor_daily_pl_updated'),
        ('Loma', '0005_auto_20190203_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='loma_attendance_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loma_attendance', models.CharField(choices=[('Started', 'Started'), ('Abandoned', 'Abandoned'), ('Finished', 'Finished')], default='A', max_length=120)),
                ('today_date', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('loma_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Loma.Loma_master')),
            ],
        ),
        migrations.CreateModel(
            name='MD_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(default='Jaipur', max_length=100)),
                ('Mandi_name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('loma_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Loma.Loma_master')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor_master')),
            ],
        ),
    ]
