from django.contrib import admin

# Register your models here.
from .models import Profile, User, UserManager

# admin.site.register(Profile)
admin.site.register(User)


