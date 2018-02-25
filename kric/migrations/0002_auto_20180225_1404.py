# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 08:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kric', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='post',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]