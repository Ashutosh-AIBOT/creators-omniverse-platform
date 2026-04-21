from django.contrib import admin
from .models import Profile, LinkItem

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_public')
    search_fields = ('user__username',)


@admin.register(LinkItem)
class LinkItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'profile', 'section', 'is_public')
    list_filter = ('section', 'is_public')
    search_fields = ('title', 'profile__user__username')
