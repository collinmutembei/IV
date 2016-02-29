from django.http import HttpResponseRedirect
from django.shortcuts import render


def landing(request):
    """renders landing page for project"""
    if request.user.is_authenticated():
        return render(request, 'dashboard.html')
    return render(request, 'landing.html')


def dashboard(request):
    """renders the projects dashboard"""
    if request.user.is_authenticated():
        return render(request, 'dashboard.html')
    return HttpResponseRedirect("/")
