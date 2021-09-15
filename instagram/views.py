from instagram.forms import signUpForm
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.conf import settings



# Create your views here.
@login_required
def home(request):
    return render(request, 'insta/index.html')

def signup(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.name, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = signUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile_info(request):
    profiles = Profile.objects.filter(user=request.user)
    if not profiles.first():
        profile = Profile.objects.create(user=request.user)
        profile.save()
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(editor=request.user)
    return render(request, 'insta/profile.html',{'profile': profile, 'posts': posts})
