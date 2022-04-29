import uuid

from django.db import models


# Create your models here.

class CourseOrder(models.Model):
    order_number = models.CharField(max_length=50, null=False, editable=False)
    # USER PROFILE LINK
    firstName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=300, null=False, blank=False)
    address_line_1 = models.CharField(max_length=100, null=False, blank=False)
    address_line_2 = models.CharField(max_length=100, null=False, blank=False)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    postCode = models.CharField(max_length=10, null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    order_cost = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    order_tax = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    order_total_cost = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_payment_id = models.CharField(null=False, blank=False, max_length=300, default='')

    def _generate_order_number(self):
        """
        Generate Order number using user id uuid
        """
        return uuid.uuid4().hex.upper()
