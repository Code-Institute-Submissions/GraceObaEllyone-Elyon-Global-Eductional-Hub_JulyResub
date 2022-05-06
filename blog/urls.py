from django.urls import path

from blog import views

urlpatterns = [
    path('add/', views.add_blog, name='add_blog')
]