from django.shortcuts import render

def main(request):
    context = {}
    return render(request, 'outside/main.html', context)

def explore(request):
    context={}
    return render(request, 'outside/explore.html', context)
    