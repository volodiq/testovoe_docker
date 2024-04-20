from django.db import models
from django.contrib.auth.models import User


class ExecutorProfile(models.Model):
    """Профили исполнителей"""
    user = models.ForeignKey(
        User,
        related_name="executor_profile",
        on_delete=models.CASCADE,
    )
    experience = models.PositiveSmallIntegerField(verbose_name="Опыт в годах", default=0)
    phone = models.CharField(null=True, blank=True, max_length=30)
