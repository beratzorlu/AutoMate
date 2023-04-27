from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Post)
class AdminPost(SummernoteModelAdmin):
    """
    Defines Post model and PostAdmin model.
    """
    summernote_fields = ('content')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'created_on', 'author', 'status')
    list_filter = ('created_on', 'status')
    search_fields = ('title', 'slug', 'created_on', 'status', 'author__username')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Defines Comment model and CommentAdmin model.
    """
    actions = ['comment_approval']
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('created_on', 'approved', 'post')
    search_fields = ('name', 'email', 'body')

    def comment_approval(self, request, queryset):
        queryset.update(approved=True)

    

