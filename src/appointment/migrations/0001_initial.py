# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-23 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinic', '0004_auto_20170823_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('appointment_day', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Doctor')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together=set([('doctor', 'appointment_day', 'start_time', 'end_time')]),
        ),
        migrations.AlterIndexTogether(
            name='appointment',
            index_together=set([('first_name', 'last_name')]),
        ),
    ]
