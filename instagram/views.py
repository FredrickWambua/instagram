from instagram.forms import signUpForm
from django.shortcuts import get_object_or_404, render,redirect, resolve_url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.conf import settings



# Create your views here.

@login_required
def profile_info(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    url_name = resolve_url(request.path).url_name
    if url_name == 'profile':
        posts = Post.objects.filter(user=user).order_by('-posted_on')
    else:
        posts = Profile.objects.all()
    return render(request, 'insta/index.html',{'profile': profile, 'posts': posts})

@login_required
def home(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    all_profiles = Profile.objects.all()
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context = {
        'user_profile': user_profile,
        'all_profiles': all_profiles,
        'posts': posts,
        'comments': comments,
    }
    return render(request, 'insta/index.html', context)

def signup(request):
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


