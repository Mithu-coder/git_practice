from django.db import models

from django.db.models.signals import post_save
from django.dispatch import  receiver
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    full_name=models.CharField(max_length=100,null=True,blank=True)
    address=models.TextField(max_length=300,null=True,blank=True)
    country=models.CharField(max_length=50,blank=True,null=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    zipcode=models.CharField(max_length=15,null=True,blank=True)
    phone=models.CharField(max_length=50,null=True,blank=True)
    data_of_birth=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profiles"

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
