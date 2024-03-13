from django.contrib import admin


class ReviewAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False
