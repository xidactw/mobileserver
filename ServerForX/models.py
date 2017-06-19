# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CameraParameters(models.Model):

	updateTime = models.DateTimeField(auto_now_add=True)
	paraFile = models.FileField('CameraParameters')






