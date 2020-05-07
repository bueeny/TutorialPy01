# Django signals > Recommneds creating a standalone file
#Django includes a “signal dispatcher” which helps allow decoupled applications get notified 
# when actions occur elsewhere in the framework.
#In a nutshell, signals allow certain senders to notify a set of receivers 
# that some action has taken place. They’re especially useful when many 
# pieces of code may be interested in the same events.

from django.db.models.signals import post_save #signal that is fired after a user profile is saved
from django.contrib.auth.models import User # sender
from django.dispatch import receiver # receiver
from .models import Profile # import models

@receiver(post_save, sender = User) # when a user is saved, send a signal. This signal will be recieved by a receiver.
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance) # Profile to be created at that instance

@receiver(post_save, sender = User) # when a user is saved, send a signal. This signal will be recieved by a receiver.
def save_profile(sender, instance, **kwargs):  
    instance.profile.save()
    
