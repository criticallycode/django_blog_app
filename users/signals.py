from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# use signals to tie functions together

# signals to create profile upon registration
# decorator works like this - when a User is saved, send a signal (User is the sender)

# the receiver is the create_profile, which takes specific arguments -
# one is the instance (which user was it) and was the profiled created? -
# if yes, also create Profile with instance of current user

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# takes in instance (current user) of saves User profile and saves it
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# after signals are created, need to be imported into apps