from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_name', 'deadline', 'finished', 'user')
    list_display_links = ['task_name']
    search_fields = ('user',)
    list_filter = ('user',)
    list_editable = ('finished',)

