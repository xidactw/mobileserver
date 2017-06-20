# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
# Create your models here.

class ThreeDModel(models.Model):
    updtime = models.CharField(max_length=100)
    age_c = models.CharField(max_length=100)
    age_e = models.CharField(max_length=100)
    likecoun = models.CharField(max_length=100)
    downcoun = models.CharField(max_length=100)
    high_e = models.CharField(max_length=100)
    audioname3 = models.CharField(max_length=100)
    audioname2 = models.CharField(max_length=100)
    audioname1 = models.CharField(max_length=100)
    qrimage1 = models.CharField(max_length=100)
    qrimage2 = models.CharField(max_length=100)
    mdesc = models.CharField(max_length=100)
    rmid = models.CharField(max_length=100)
    mid = models.CharField(max_length=100)
    wide_e = models.CharField(max_length=100)
    htmlpage = models.CharField(max_length=100)
    addtime = models.CharField(max_length=100)
    tid = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100)
    wide_c = models.CharField(max_length=100)
    mpath = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    high_c = models.CharField(max_length=100)
    coldesc = models.CharField(max_length=100)
    ext_1 = models.CharField(max_length=100)
    name_c = models.CharField(max_length=100)
    name_e = models.CharField(max_length=100)
    md5 = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    material_c = models.CharField(max_length=100)
    material_e = models.CharField(max_length=100)
    intro_c = models.CharField(max_length=100)
    intro_e = models.CharField(max_length=100)
    colimage = models.CharField(max_length=100)
    authoity = models.CharField(max_length=100)
    bgImageName1 = models.CharField(max_length=100, default="")
    bgImageName2 = models.CharField(max_length=100, default="")

    def __unicode__(self):
        return str(self.id) + '-' + self.mname + '-' + self.mid


class App_3DModel_List(models.Model):
    threeDModel = models.ForeignKey(ThreeDModel)
    tname = models.CharField(max_length=100, default="")
    listImagePath = models.TextField()
    lastUpdate = models.DateField(auto_now=True)

    def __unicode__(self):
        return str(self.threeDModel.id) + '-' + self.threeDModel.mname


class App_3DModel_list_B(models.Model):
    # threeDModel = models.ForeignKey(ThreeDModel)
    celImage = models.ImageField(upload_to="static")

@receiver(post_delete, sender=App_3DModel_list_B)
def photo_post_delete_handler(sender, **kwargs):
    photo = kwargs['instance']
    storage, path = photo.celImage.storage, photo.celImage.path
    storage.delete(path)

