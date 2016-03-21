from django.http import HttpResponseRedirect
from django.shortcuts import render


def landing(request=None):
    """render the landing page"""
    if request.user.is_authenticated():
        return HttpResponseRedirect("/app")
    return render(request, 'landing.html')


def dashboard(request):
    """renders the projects dashboard"""
    if request.user.is_authenticated():
        return render(request, 'dashboard.html')
    return HttpResponseRedirect("/")
