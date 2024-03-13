from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from app.models import ExtendedUser


class ExtendedUserAdmin(admin.StackedInline):
    model = ExtendedUser
    can_delete = False
    verbose_name_plural = "Корисници"
    readonly_fields = ("favorites",)


class UserAdmin(BaseUserAdmin):
    inlines = [ExtendedUserAdmin]
