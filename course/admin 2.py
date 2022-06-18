from django.contrib import admin

# Register your models here.
from course.models import Course, CourseReview, Category

admin.site.register(Course)
admin.site.register(CourseReview)
admin.site.register(Category)