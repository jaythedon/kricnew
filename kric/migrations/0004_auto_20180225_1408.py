# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 08:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kric', '0003_auto_20180225_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+918112292576'. Up to 15 digits allowed.", regex='^\\+?91?\\d{9,11}$')]),
        ),
    ]
