from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View


def landing(request=None):
    """redirects user to web app"""
    return HttpResponseRedirect("/web/")


def dashboard(request):
    """renders the projects dashboard"""
    return render(request, 'dashboard.html')


class applyeffects(View):
    """"view to apply effects to image"""
    def post(self, request):
        effects = request.body
        return effects
