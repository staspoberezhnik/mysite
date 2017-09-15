from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 2


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content']
    inlines = [CommentInline]
    list_filter = ['date_created']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
# admin.site.register(Tag)