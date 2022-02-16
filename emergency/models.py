from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    """
    The model for a car that is registered in the system.

    Attributes:
        name (str): The name of the car or the license plate.
        user (User): The user that owns the car.
        has_accident (bool): Whether the car has an accident or not.
    """
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, blank=True)
    has_accident = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Location(models.Model):
    """
    The model for a user's location that's tracked in the system.

    Attributes:
        user (User): The user that's location is being tracked.
        lat (float): The latitude of the location.
        lng (float): The longitude of the location.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Location"
