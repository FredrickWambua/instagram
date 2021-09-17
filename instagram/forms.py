from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from .models import User, Profile, UserManager, Post, Comment

class signUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=255, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username','email',)

class UploadPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'likes', 'name', 'posted']


