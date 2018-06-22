# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class UrlShorter(models.Model):
    key = models.CharField(max_length=10, primary_key=True)
    url = models.URLField(max_length=250, unique=True)
    last_enter_url = models.URLField(max_length=250)
