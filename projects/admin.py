from django.contrib import admin
from . import models

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'link_git', 'link_view')
    list_filter = ('title', )
    # ordering = ('title', )
    search_field = ('title')
admin.site.register(models.Project, ProjectAdmin)


# testing my commits
