from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "created_at")
    search_fields = ("username", "message")
    list_filter = ("created_at",)
    ordering = ("-created_at",)