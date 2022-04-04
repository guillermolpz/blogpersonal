from re import search
from django.contrib import admin

from .models import Blog

# Register your models here.
#admin.site.register(Blog)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','imagen','titulo','descripcion','created')
    list_display_links = ('id','titulo',)
    
    list_filter = ('created','update')
    search_fields = ('titulo','descripcion')
    
    readonly_fields = ('created','update')