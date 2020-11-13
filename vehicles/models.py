from django.db import models
from django.utils import timezone


class Specification(models.Model):
    plate_number = models.CharField(max_length=10, unique=True)
    PETROL = 'P'
    DIESEL = 'D'
    # ELECTRONIC = 'E'
    FUEL_TYPE_CHOICES = [
        (PETROL, 'Petrol'),
        (DIESEL, 'Diesel')
    ]
    fuel_type = models.CharField(max_length=1, choices=FUEL_TYPE_CHOICES)
    odometer = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    odo_date_as_of = models.DateField(blank=True, null=True, default=timezone.now)
    other_details = models.TextField(blank=True, null=True)
