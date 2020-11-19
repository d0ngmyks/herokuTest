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

    def __str__(self):
        return str(
            {'id': f'{self.pk}',
             'plate_number': f'{self.plate_number}',
             'fuel_type': f'{self.fuel_type}',
             'odometer': f'{self.odometer}',
             'odo_date_as_of': f'{self.odo_date_as_of}',
             'other_details': f'{self.other_details}'}
        )
