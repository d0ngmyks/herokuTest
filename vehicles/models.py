from django.db import models
from django.utils import timezone


class Specification(models.Model):
    plate_number = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=10, blank=True)
    odometer = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    odo_date_as_of = models.DateField(blank=True, null=True, default=timezone.now)
    front_tire_psi = models.IntegerField(default=30)
    rear_tire_psi = models.IntegerField(default=30)
