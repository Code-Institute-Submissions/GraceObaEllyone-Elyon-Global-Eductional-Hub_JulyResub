from django.contrib import admin

# Register your models here.
from .models import BlogPost, BlogImage, BlogComment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class PostImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'blog_post_id')


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('blog_post_id', 'comment_title', 'comment_desc',
                    'created_on')
    search_fields = ['comment_desc']


admin.site.register(BlogPost, BlogAdmin)
admin.site.register(BlogImage, PostImageAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
