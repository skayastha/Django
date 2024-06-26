from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello!")


def newPage(request):
    return HttpResponse("Welcome to New Page!")


def summit(request):
    return HttpResponse("Hello Summit!")

def greet(request, name):
    return HttpResponse(f"Hello {name}")


