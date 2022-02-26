from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
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


@admin.register(models.User)
class UserAdmin(UserAdmin):
    """ User Admin Definition """
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'name', 'bio', 'avatar')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
