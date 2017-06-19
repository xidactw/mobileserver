# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import ThreeDModel
from .models import App_3DModel_List
# Register your models here.

admin.site.register(ThreeDModel)
admin.site.register(App_3DModel_List)
