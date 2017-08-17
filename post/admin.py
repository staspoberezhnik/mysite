from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class PostInline(admin.StackedInline):
    model = Comment
    extra = 2


class PostAdmin(admin.ModelAdmin):
    fields = ['post_title', 'post_content']
    inlines = [PostInline]
    list_filter = ['post_date_created']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
# admin.site.register(Tag)