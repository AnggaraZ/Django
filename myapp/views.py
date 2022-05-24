from django.shortcuts import render
from django.template import loader

# Create your views here.

def beranda(request):
    return render(request, 'beranda.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def login(request):
    return render(request, 'login.html')


