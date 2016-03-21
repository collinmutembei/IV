from django.shortcuts import render


def landing(request):
    """load the app"""
    return render(request, 'index.html')
