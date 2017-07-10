# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from models import RegistryModel

class RegistryModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(RegistryModel, RegistryModelAdmin)
