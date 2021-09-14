from os import name

from django.db.models.deletion import CASCADE
from instaclone.settings import TIME_ZONE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from cloudinary.models import CloudinaryField
import datetime


# Create your models here.
# class UserManager(AbstractUser):

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        '''
        Creates and saves a User with the given email and password.
        '''
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email)),
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        '''
        Creates and saves a staff user with a given email and password.
        '''
        user = self.create_user(email, password=password,)
        user.staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        '''
        Creates and saves a superuser with the given email and password.
        '''
        user = self.create_user(email, password=password,)
        user.staff(using=self._db)
        return user
        
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, null=True)
    email= models.EmailField(default=False)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=255)
    joined = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    


class Post(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=80, blank=True)
    caption = models.CharField(max_length=255, blank=True)
    likes = models.ManyToManyField(CustomUser, related_name='likes', blank=True)
    posted_on = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.user.name} Post '


class Comment(models.Model):
    comment = models.TextField(max_length=255)
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=CASCADE, related_name='comments')
    commented_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.name} Comment '

