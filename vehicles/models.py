from django.db import models
from django.utils import timezone


class Specification(models.Model):
    plate_number = models.CharField(max_length=10, unique=True)
    fuel_type = models.CharField(max_length=1)
    odometer = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    odo_date_as_of = models.DateField(blank=True, null=True, default=timezone.now)
    other_details = models.TextField(blank=True, null=True)
