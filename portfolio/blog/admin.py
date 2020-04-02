from django.contrib import admin
from .models import Blog

# admin.site.register(Blog)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)
    ordering = ('-date',)
