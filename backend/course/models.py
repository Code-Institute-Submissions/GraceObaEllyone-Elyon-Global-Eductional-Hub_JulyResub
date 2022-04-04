import django.utils.timezone
from django.db import models

# Create your models here.
from django.db import models


from django.db import models


# https://docs.djangoproject.com/en/4.0/topics/db/examples/
class User(models.Model):
    userId = models.IntegerField(unique=True, blank=False, auto_created=True).primary_key
    email = models.EmailField(unique=True, blank=False, default=None)
    password = models.CharField(max_length=256, blank=False, default=None)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField(null=True)
    gender = models.CharField(max_length=1, null=True)
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    contact_number = models.CharField(max_length=20, null=True)
