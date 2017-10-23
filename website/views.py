from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from website.forms import (
    RegistrationForm, 
    EditProfileForm
)
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login
from .models import UserProfile
from .models import NewUser
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView
from website.forms import HomeForm
from website.models import Post
from django.conf.urls import url
#

def home(request):
    numbers = [1,2,3,4,5]
    name = 'Marco Chow'

    args = {'myName': name, 'numbers': numbers}
    return render(request, 'website/welcome.html', args)
    
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/website/detail/')
        else:
            return HttpResponse("not ok")
    else:
        form = RegistrationForm()

        args = {'form': form}
        # a-ccounts here is in "templates"
        return render(request, 'website/reg_form.html', args) 

def view_profile(request):
    args = {'user': request.user}
    return render(request, '/website/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('website/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'website/edit_profile.html', args)

# @login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'website/profile.html', args)

# @login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('website/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'website/edit_profile.html', args)

# @login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('website/profile')
        else:
            return redirect('website/change-password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'website/change_password.html', args)

class HomeView(TemplateView):
    template_name = 'website/detail.html'
    
    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all()
        args = {'form':form, 'posts':posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            args = {'post':post}
            # text = form.cleaned_data['post']
            # form = HomeForm()
            return render(request, '/website/', args)

        args = {'form':form}
        return render(request, self.template_name, args)

def search(request):
    return render(request, 'website/search.html')

# -----------------------------------------------------

def statelibraryofqueensland(request):
    return render(request, 'website/statelibraryofqueensland.html')

def qutgardenspointlibrary(request):
    return render(request, 'website/qutgardenspointlibrary.html')

def brisbanesquarelibrary(request):
    return render(request, 'website/brisbanesquarelibrary.html')

def citybotanicgardens(request):
    return render(request, 'website/citybotanicgardens.html')

def kangaroopointcliffspark(request):
    return render(request, 'website/kangaroopointcliffspark.html')

def romastreetparkland(request):
    return render(request, 'website/romastreetparkland.html')

def storybridge(request):
    return render(request, 'website/storybridge.html')
    
def victoriabridge(request):
    return render(request, 'website/victoriabridge.html')

def kurilpabridge(request):
    return render(request, 'website/kurilpabridge.html')

def goodwillbridge(request):
    return render(request, 'website/goodwillbridge.html')

def angelospastafactory(request):
    return render(request, 'website/angelospastafactory.html')

def noosachocolatefactory(request):
    return render(request, 'website/noosachocolatefactory.html')

def theglassfactory(request):
    return render(request, 'website/theglassfactory.html')

def queenslandpolicemuseum(request):
    return render(request, 'website/queenslandpolicemuseum.html')

def queenslandpolicemuseum(request):
    return render(request, 'website/queenslandpolicemuseum.html')

def queenslandmuseumandsciencentre(request):
    return render(request, 'website/queenslandmuseumandsciencentre.html')

def museumofbrisbane(request):
    return render(request, 'website/museumofbrisbane.html')
