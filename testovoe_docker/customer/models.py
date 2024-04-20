from django.db import models
from django.contrib.auth.models import User


class CustomerProfile(models.Model):
    """Профили заказчиков"""
    user = models.ForeignKey(
        User,
        related_name="customer_profile",
        on_delete=models.CASCADE,
    )
    phone = models.CharField(null=True, blank=True, max_length=30)
