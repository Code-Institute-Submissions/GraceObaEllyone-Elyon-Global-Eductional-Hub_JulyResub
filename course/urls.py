from django.urls import path
from course import views

urlpatterns = [
    path('', views.all_course, name='all_courses'),
    path('add/', views.add_course, name='add_course'),
    path('category/add/', views.add_category, name='add_category'),
    path('<int:course_pk>', views.single_course, name='single_course'),
    path('edit/<int:course_pk>', views.edit_course, name='edit_course'),
    path('delete/<int:course_pk>', views.delete_course, name='delete_course')
]
