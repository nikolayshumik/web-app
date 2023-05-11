from django.shortcuts import render
from .models import Raspisanie


def index(request):
    news = Raspisanie.objects.all()
    return render(request, 'main/index.html', {'news': news})

def about(request):
    news = Raspisanie.objects.all()
    return render(request, 'main/about.html', {'news': news})

def create(request):
    news = Raspisanie.objects.all()
    return render(request, 'main/create.html', {'news': news})

def afisha(request):
    news = Raspisanie.objects.all()
    return render(request, 'main/afisha.html', {'news': news})

def book(request):
    news = Raspisanie.objects.all()
    return render(request, 'main/book.html', {'news': news})

def shema(request):
    news = Raspisanie.objects.all()
    return render(request, 'main/shema.html', {'news': news})
