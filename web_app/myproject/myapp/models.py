# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=1000, default="")
    publisher = models.CharField(max_length=1000, default="")
    link = models.CharField(max_length=1000, default="")
    cluster = models.CharField(max_length=1000, default="")
    bias = models.FloatField(default=.0)
    cred = models.FloatField(default=.5)
