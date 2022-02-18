from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile, FirstLogin
from emergency.models import Location
from django.dispatch.dispatcher import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Location.objects.create(user=instance)
        FirstLogin.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """Signal when user change something in profile, it will save."""
    instance.profile.save()