from django.http import HttpResponseRedirect
from django.shortcuts import render


def landing(request):
    """redirects user to web app"""
    return HttpResponseRedirect("/web/")


def dashboard(request):
    """renders the projects dashboard"""
    return render(request, 'dashboard.html')
