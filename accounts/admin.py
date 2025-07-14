from django.contrib import admin
from accounts.models.profile import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'birth_date', 'gender')
    search_fields = ('user__username', 'full_name')

