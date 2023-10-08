from django.contrib import admin
from .models import Task


class Todoadmin(admin.ModelAdmin):
    list_display = ["Title", "Description", "Completed"]

admin.site.register(Task, Todoadmin)