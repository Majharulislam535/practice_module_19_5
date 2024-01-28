from django.shortcuts import render
from django.views.generic import ListView
from album.models import Album_Model


class HomeView(ListView):
    model = Album_Model
    template_name='index.html'
    context_object_name='data'


