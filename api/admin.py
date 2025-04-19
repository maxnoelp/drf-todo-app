from django.contrib import admin
from .models import Todo, Skill, Projects

admin.site.register(Todo)
admin.site.register(Skill)


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("title", "coding_language", "created_at", "updated_at", "published")
    list_filter = ("coding_language", "created_at", "updated_at", "published")
    search_fields = ("title", "coding_language")
    ordering = ("created_at",)


admin.site.register(Projects, ProjectsAdmin)
