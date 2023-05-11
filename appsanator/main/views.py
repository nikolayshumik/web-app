from django.shortcuts import render
from .models import Raspisanie


def index(request):
    news = Raspisanie.objects.all()
    return render(request, 'main/index.html', {'news': news})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    return render(request, 'main/create.html')

