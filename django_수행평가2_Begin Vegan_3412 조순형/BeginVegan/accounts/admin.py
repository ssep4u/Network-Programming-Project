from django.contrib import admin

from accounts.models import Profile


@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    list_display_links = ['user']
    search_fields = ['user']