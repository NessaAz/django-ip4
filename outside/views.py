from multiprocessing import context
from django.shortcuts import render

def main(request):
    context = {}
    return render(request, 'outside/main.html', context)

def explore(request):
    context={}
    return render(request, 'outside/explore.html', context)
    
def login(request)    :
    context={}
    return render(request, 'outside/login.html', context)

def signup(request)    :
    context={}
    return render(request, 'outside/signup.html', context)