from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def newPage(request):
    return HttpResponse("Welcome to New Page!")

def summit(request):
    return HttpResponse("Hello Summit!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })



