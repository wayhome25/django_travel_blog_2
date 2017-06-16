from django.contrib import admin
from .models import Comment, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_public', 'created_at']
    list_display_links = ['title']
    list_editable = ['is_public']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'author', 'post']
    list_display_links = ['message']
