from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def salam(request):
    return HttpResponse("wellcome to my code")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')


