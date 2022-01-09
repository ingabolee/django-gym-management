from django.contrib import admin
from django.contrib.auth.models import Group
from . import models

admin.site.register(models.Customer)
admin.site.register(models.Subscription)
admin.site.register(models.Payment)
admin.site.register(models.Workout)
admin.site.register(models.Equipment)
admin.site.register(models.Event)
admin.site.unregister(Group)
