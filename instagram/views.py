from django.http.response import HttpResponseRedirect
from instagram.forms import SignUpForm, UploadPostForm, CommentForm, UpdateUserForm, UpdateProfileForm
from django.shortcuts import get_object_or_404, render,redirect, resolve_url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt





# Create your views here.

@login_required(login_url='login')
def profile(request):
    profiles = Profile.objects.filter(user=request.user)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.url_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateProfileForm(instance=request.user.profile)
    context = {
    'user_form': user_form,
    'prof_form': prof_form,
    'profiles': profiles,
            }
            
    return render(request, 'insta/profile.html', context)

@login_required
def home(request):
    user = request.user
    # user_profile = Profile.objects.get(user=user)
    all_profiles = Profile.objects.all()
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context = {
        # 'user_profile': user_profile,
        'all_profiles': all_profiles,
        'posts': posts,
        'comments': comments,
    }
    return render(request, 'insta/index.html', context)

def signup(request):
    if request.method == 'POST':     
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username} Your account was created successfully. ')
            return redirect('home')
    else:
        form = SignUpForm
    return render(request, 'registration/signup.html', {'form': form} )

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class= UploadPostForm
    template_name = 'insta/post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



@csrf_exempt
def search(request):
    if request.method=='GET':
        result = request.GET.get('q')
        if result:
            display = Post.objects.filter(Q(name__icontains = result)|Q(caption__icontains = result))
            return render(request, 'insta/search.html',  {'display': display})
            
        else:
            message = "No information found from your search. Try to refine your search term"
            return render(request, 'insta/search.html',{"message":message})