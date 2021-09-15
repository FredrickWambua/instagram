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

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        '''
        Creates and saves a User with the given email and password.
        '''
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email),)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        '''
        Creates and saves a staff user with a given email and password.
        '''
        user = self.create_user(email, password=password,)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        '''
        Creates and saves a superuser with the given email and password.
        '''
        user = self.create_user(email, password=password,)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active



    objects =UserManager()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, null=True)
    email= models.EmailField(default=False)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=255)
    joined_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    


class Post(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=80, blank=True)
    caption = models.CharField(max_length=255, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
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

