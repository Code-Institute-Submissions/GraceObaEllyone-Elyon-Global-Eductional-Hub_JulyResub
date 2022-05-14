from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=500)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    requirement = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    duration = models.IntegerField(default=0)
    courseImage = models.ImageField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def duration_hour(self):
        return int(self.duration / 60)

    @property
    def duration_min(self):
        return self.duration % 60

    def __str__(self):
        return 'title: {}'.format(self.title)


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CourseReview(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    course = models.ForeignKey('Course', null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    rating_score = models.IntegerField(choices=RATING_CHOICES, default=0)
    review_title = models.CharField(max_length=254)
    review_comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True, verbose_name='review_created_date')

    @property
    def review_rate(self):
        return self.rating_score / 5 * 100

    def __str__(self):
        return 'user: {}, review_title: {}'.format(self.user_id, self.review_title)
