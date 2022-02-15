from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    has_accident = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Location"
