from django.db import models

# Create your models here.
from django.db import models


class Property(models.Model):
    address = models.CharField(max_length=255)
    size = models.FloatField()
    price = models.FloatField()
    comments = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=16)
    location = models.ForeignKey('City', null=True, on_delete=models.SET_NULL, related_name='property')

    def __str__(self):
        return f'{self.address} {self.size} {self.price} '


class City(models.Model):
    name = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    life_index = models.FloatField()

    def __str__(self):
        return f'{self.name}'