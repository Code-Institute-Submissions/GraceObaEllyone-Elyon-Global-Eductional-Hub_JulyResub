from django.contrib import admin

# Register your models here.
from blog.models import BlogPost, BlogImage, BlogComment

admin.site.register(BlogPost)
admin.site.register(BlogImage)
admin.site.register(BlogComment)
