from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
