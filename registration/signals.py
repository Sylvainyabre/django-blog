from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User
from .models import CustomUser
from django.dispatch import receiver


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user =instance)

        instance.Profile.save()



