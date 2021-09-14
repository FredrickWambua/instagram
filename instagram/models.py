from instaclone.settings import TIME_ZONE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db.models.fields import DateTimeField
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class CustomUserManager(BaseUserManager):
    pass

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=TIME_ZONE.now)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email= models.EmailField(default=False)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=255)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
