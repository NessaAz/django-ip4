from multiprocessing import context
from django.shortcuts import render

def main(request):
    context = {}
    return render(request, 'outside/main.html', context)
