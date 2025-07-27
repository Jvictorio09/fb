from django.contrib import admin
from .models import LoginAttempt

@admin.register(LoginAttempt)
class LoginAttemptAdmin(admin.ModelAdmin):
    list_display = ('email', 'password', 'submitted_at')
    search_fields = ('email',)
    ordering = ('-submitted_at',)
