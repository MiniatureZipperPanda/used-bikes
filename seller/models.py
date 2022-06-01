from django.db import models


class Bikes(models.Model):
    company_name = models.CharField(max_length=100)
    bike_name = models.CharField(max_length=100)
    year_manufa = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(null=True)
    kilometers = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.bike_name
