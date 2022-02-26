from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """
    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """ Message Admin Definition """
    pass


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    """ Topic Admin Definition """
    pass
