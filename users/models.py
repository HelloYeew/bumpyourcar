"""Database models for the users app."""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    The additional profile information for the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    personal_id = models.BigIntegerField(default=0)
    address = models.TextField(default='', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class FirstLogin(models.Model):
    """
    The field to check is user success the first login prompt or not.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_login = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} first login prompt check [{self.first_login}]'
