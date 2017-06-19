# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App_3DModel_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listImagePath', models.TextField()),
                ('lastUpdate', models.DateField(auto_now=True)),
                ('threeDModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellt.ThreeDModel')),
            ],
        ),
    ]
