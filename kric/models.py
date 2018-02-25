# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Post(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?91?\d{9,11}$', message="Phone number must be entered in the format: '+918112292576'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list



    def publish(self):
        self.save()
    def kk(self):
        return self.phonenumber
