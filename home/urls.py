from django.urls import path
from. import views


urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus', views.aboutUs, name='aboutus'),
    path('contactform', views.contactform, name='contactform'),
#     path('thankyou_page/', views.thankyou_page, name='thankyou_page'),
]
