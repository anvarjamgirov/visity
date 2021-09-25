from django.db import models
from django.utils import timezone


class Worker(models.Model):
    first_name = models.CharField(
        max_length=127
    )
    phone_number = models.CharField(
        max_length=31,
        unique=True
    )

    def __str__(self):
        return self.first_name


class Outlet(models.Model):
    name = models.CharField(
        max_length=127
    )
    worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        related_name='outlets'
    )

    def __str__(self):
        return self.name


class Visit(models.Model):
    date = models.DateTimeField(
        default=timezone.now
    )
    coordinates = models.CharField(
        max_length=63
    )
    outlet = models.ForeignKey(
        Outlet,
        on_delete=models.CASCADE,
        related_name='visits'
    )

    def __str__(self):
        return f"{self.outlet.worker} came to {self.outlet}({self.coordinates}) in {self.date}"
