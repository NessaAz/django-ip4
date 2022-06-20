from multiprocessing import context
from django.shortcuts import render
from .models import *


def main(request):
    context = {}
    return render(request, 'outside/main.html', context)

def explore(request):
    neighbourhoods=Neighborhood.objects.all()
    business=Business.objects.all()
    posts=Post.objects.all()
    # comments=Comment.objects.all()
    # likes=Like.objects.all()
    profiles=Profile.objects.all()
    context = {'neighbourhoods': neighbourhoods}
    context = {'business': business}
    context = {'posts': posts}
    context = {'profiles': profiles}
    return render(request, 'outside/explore.html', context)
    
def login(request)    :
    context={}
    return render(request, 'outside/login.html', context)

def signup(request)    :
    context={}
    return render(request, 'outside/signup.html', context)

def hoods(request):
    neighbourhoods = Neighborhood.objects.all()
    context = {'neighbourhoods': neighbourhoods}
    return render(request, 'outside/hoods.html', context)