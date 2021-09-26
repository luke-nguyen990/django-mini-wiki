from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("wiki/edit/<str:title>", views.edit, name="edit"),
    path("wiki/search/", views.search, name="search"),
    path("wiki/create/", views.create, name="create"),    
    path("wiki/save/", views.save, name="save"),
    path("wiki/random/", views.random, name="random")  
]
