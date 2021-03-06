from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields, widgets
from .models import User, Profile, UserManager, Post, Comment


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=255, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=255, help_text='Required. Inform a valid email address')

    class Meta:
        model = User
        fields = ('username', 'email')
        exclude = ['user']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'profile_photo', 'bio')
        exclude = ['user']

class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ['user']

class UploadPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'likes', 'name', 'posted']

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)
    class Meta:
        model = Comment
        fields = ('author', 'body',)


