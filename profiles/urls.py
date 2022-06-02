from django.urls import path

from profiles import views

urlpatterns = [
    path('update/', views.update_details, name='update_profile'),
]