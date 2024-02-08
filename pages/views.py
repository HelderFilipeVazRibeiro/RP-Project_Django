# pages/views.py

from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {})

def home2(request):
    return render(request, "pages/home2.html", {})

def login(request):
    return render(request, "pages/login.html", {} )

def register(request):
    return render(request, "pages/register.html", {} )

