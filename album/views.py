from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Album_Model
from .forms import Album
# Create your views here.

@method_decorator(login_required,name='dispatch')

class Create_Album(CreateView):
    model= Album_Model
    form_class = Album
    template_name = 'album.html'
    success_url = reverse_lazy('home')

@method_decorator(login_required,name='dispatch')

class Edit_Album(UpdateView):
    model= Album_Model
    form_class = Album
    template_name = 'album.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('home')
