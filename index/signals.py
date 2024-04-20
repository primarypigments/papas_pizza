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


@receiver(user_signed_up)
def user_signed_up(request, user, **kwargs):
    """
    Handles post-signup actions: logs signup and creates a user profile.
    """
    # Log the user signup
    print(f"New user signed up: {user.email}")
    # Create a user profile instance
    UserProfile.objects.create(
        user=user,
        # Initialize any default or blank fields, if necessary
        phone_number='',
        street_address='',
        city='',
        zip_code=''
    )
    print(f"Profile created for {user.email}")