from django.db import models


# Create your models here.


class Payment(models.Model):
    gfd = models.IntegerField()
    paymentDate = models.DateField(auto_now=True)

