from django.contrib import admin

# Register your models here.
from profiles.models import UserProfile, UserGroup

admin.site.register(UserProfile)
admin.site.register(UserGroup)