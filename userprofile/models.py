from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete="CASCADE")
    phone_number = models.CharField(max_length =20)
    no_of_years_in_fishery = models.IntegerField(null=True,blank=True)
    state = models.CharField(max_length = 100)
    district = models.CharField(max_length = 100)
    created_date = models.DateField(auto_now=True,auto_now_add=False)
    updated_date = models.DateField(auto_now=False, auto_now_add=True)
   

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)