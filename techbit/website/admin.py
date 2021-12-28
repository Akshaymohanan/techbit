from django.contrib import admin
from .models import Projects

# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name','description','image','date']
    list_editable = ['name','description','image','date']
    admin.site.register(Projects)
