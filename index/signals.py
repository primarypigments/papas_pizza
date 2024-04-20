from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import PizzaUserProfile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creates or updates the user profile after a User instance is saved.
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

