from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def main(request):
    context = {}
    return render(request, 'outside/main.html', context)

def explore(request):
    neighbourhoods=Neighborhood.objects.all()
    # business=Business.objects.all()
    # posts=Post.objects.all()
    # comments=Comment.objects.all()
    # likes=Like.objects.all()
    # profiles=Profile.objects.all()
    
    context = {'neighbourhoods': neighbourhoods}
    # context = {'business': business}
    # context = {'posts': posts}
    # context = {'profiles': profiles}
    return render(request, 'outside/explore.html', context)

# def login(request)    :
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#         return redirect('hoods')
#     else:
#         form = LoginForm()
#     return render(request, 'outside/login.html')
def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user_obj = form.cleaned_data.get('user_obj')
            login(request, user_obj)
            return redirect('hoods') # if you want to redirect same page then, return redirect('this function name in urls.py')

    return render(request, 'outside/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'outside/signup.html', {'form': form})

def hoods(request):
    neighbourhoods = Neighborhood.objects.all()
    context = {'neighbourhoods': neighbourhoods}
    return render(request, 'outside/hoods.html', context)

def business(request):
    business = Business.objects.all()
    context = {'business': business}
    return render(request, 'outside/business.html', context)

def businessdetail(request):
    # business = Business.objects.all()
    context = {'business': business}
    return render(request, 'outside/businessdetail.html', context)

def profile(request):
    profile = Profile.objects.all()
    context = {'profile': profile}
    return render(request, 'outside/profile.html', context)

def post(request):
    post = Post.objects.all()
    context = {'post': post}
    return render(request, 'outside/post.html', context)