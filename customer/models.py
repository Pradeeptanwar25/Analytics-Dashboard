from django.db import models

from .choice import GENDER_CHOICE


class Customer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    age = models.PositiveSmallIntegerField()
    favorite_number = models.PositiveSmallIntegerField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (ID: {self.id})"
