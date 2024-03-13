from django.contrib import admin


class WineryAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False
