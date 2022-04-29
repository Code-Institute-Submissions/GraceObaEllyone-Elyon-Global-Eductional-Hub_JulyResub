from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=500)
    category = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)


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
