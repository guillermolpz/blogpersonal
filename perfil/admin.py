import imp
from django.contrib import admin

from .models import Project

# Register your models here.

#admin.site.register(Project)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','descripcion','created','update')
    list_display_links = ('id',)
    list_editable = ('titulo',)
    
    list_filter = ('created','update')
    search_fields = ('titulo','descripcion')
    
    readonly_fields = ('created','update')

