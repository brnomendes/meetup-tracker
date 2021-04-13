from django.db import models


class Location(models.Model):
    """
    Model that represents a Location.
    """

    name = models.CharField(max_length=256, blank=True)
    address_1 = models.CharField(max_length=256, blank=True)
    address_2 = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    state = models.CharField(max_length=256, blank=True)
    country = models.CharField(max_length=256, blank=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)
