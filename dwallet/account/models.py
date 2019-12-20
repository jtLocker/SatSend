from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

#Creating Profile model to add profile pictures to User model
#
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image', blank=True)

    #Used to display names on admin
    def __str__(self):
        return self.user.username
    
    #helper function for navbar template 
    def image_exist(self):
        if self.image != "":
            return True
        else:
            return False
    
#Whenever a new user is created, a profile is also created for the user in a OneToOne relationship
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#Save the profile
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()