from django.contrib import admin
from .models import Post, Comment

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status') # отопбражать в таблице данные калонки
    list_filter = ('status', 'created', 'publish', 'author')
    prepopulated_fields = {'slug': ('title',)}  # slug будет формироваться автоматически из title
    raw_id_fields = ('author',) # Новая страка посика для калонки author
    date_hierarchy = 'publish'
    ordering = ('status', 'publish') # Сартировка таблицы по status и publish

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')