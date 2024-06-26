from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:name>", views.greet, name = "greet"),
    path("newPage", views.newPage, name = "newPage"),
    path("summit", views.summit, name="summit")
]
