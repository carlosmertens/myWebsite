from django.shortcuts import render
from .models import Portfolio


def index(request):
    projects = Portfolio.objects
    return render(request, 'portfolio/index.html', {'projects': projects})
