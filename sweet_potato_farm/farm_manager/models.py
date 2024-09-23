from django.db import models

class Harvest(models.Model):
    date = models.DateField()
    quantity = models.FloatField()  # in kg
    profit = models.FloatField()     # in currency
    reinvestment_percentage = models.FloatField()  # percentage

    def __str__(self):
        return f"Harvest on {self.date}: {self.quantity}kg"

    @property
    def reinvestment_amount(self):
        return self.profit * (self.reinvestment_percentage / 100)

class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    harvests = models.ManyToManyField(Harvest)

    def __str__(self):
        return self.name
