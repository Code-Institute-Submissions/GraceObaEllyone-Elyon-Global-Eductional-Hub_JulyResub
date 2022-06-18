from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userPicture = models.ImageField(null=False, blank=True)
    default_email = models.EmailField(max_length=300, null=False, blank=False)
    default_postcode = models.CharField(max_length=20, null=False, blank=True)
    default_town = models.CharField(max_length=40, null=False, blank=True)
    default_address_1 = models.CharField(max_length=100, null=False, blank=True)
    default_address_2 = models.CharField(max_length=100, null=False, blank=True)
    default_country = models.CharField(max_length=80, null=False, blank=True)

    def __str__(self):
        return '{}, {}'.format(self.user, self.default_email)


@receiver(post_save, sender=User)
def create_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


class UserGroup(models.Model):
    name = models.CharField(max_length=50)
    type = models.IntegerField(max_length=2)
