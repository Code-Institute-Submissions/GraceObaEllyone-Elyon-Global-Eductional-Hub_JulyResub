
from django.urls import path

from blog import views

urlpatterns = [
    path('', views.all_blog, name='all_blog'),
    # path('category_view/<str:category>/', views.category_view,
    #      name='category_view'),
    path('<slug:slug>/', views.single_post, name='single_post'),
    # path('delete_comment/<int:comment_pk>', views.delete_comment,
    #      name='delete_comment'),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<int:blog_pk>/', views.edit_blog, name='edit_blog'),
    # path('delete/<int:blog_pk>/', views.delete_blog, name='delete_blog'),
]