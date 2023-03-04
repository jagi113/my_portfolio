from django.contrib import admin
from projects.models import Project, Tag

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    
    

admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)