from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Team, Folder, List, Task, Webhook  # , Space


class ListInline(admin.TabularInline):
    model = List
    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 3, "cols": 36})},
    }
    readonly_fields = ("clickup_id", "name", "description")


class TaskInline(admin.TabularInline):
    model = Task
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": "20"})},
        models.TextField: {"widget": Textarea(attrs={"rows": 3, "cols": 36})},
    }
    fields = ("is_active", "clickup_id", "name", "description")
    readonly_fields = (
        "clickup_id",
        "name",
        "description",
        "user",
    )


class TeamAdmin(admin.ModelAdmin):
    list_display = ["clickup_id", "name", "is_active"]


class SpaceAdmin(admin.ModelAdmin):
    list_display = ["clickup_id", "name", "is_active"]
    readonly_fields = ("clickup_id", "name", "description", "team")


class FolderAdmin(admin.ModelAdmin):
    inlines = (ListInline,)
    list_display = ["clickup_id", "name", "is_active"]
    readonly_fields = ("clickup_id", "name", "description", "space")


class ListAdmin(admin.ModelAdmin):
    inlines = (TaskInline,)
    list_display = ["clickup_id", "name", "is_active"]
    readonly_fields = ("clickup_id", "name", "description", "folder")


class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "clickup_id",
        "name",
        "is_active",
        "list_clickup_id",
        "list_name",
        "user_name",
        "user_email",
    ]
    readonly_fields = (
        "clickup_id",
        "name",
        "description",
        "created_json",
        "updated_json",
        "_list",
        "user",
    )


class WebhookAdmin(admin.ModelAdmin):
    list_display = ["clickup_id", "team"]
    readonly_fields = ("clickup_id", "team", "created_json")


admin.site.register(Team, TeamAdmin)
# admin.site.register(Space, SpaceAdmin)
admin.site.register(Folder, FolderAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Webhook, WebhookAdmin)
