from django.contrib import admin

# Register your models here.

from . models import Course, Image, CourseReview

admin.site.register(Course)
admin.site.register(Image)
admin.site.register(CourseReview)