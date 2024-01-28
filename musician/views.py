from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Musicians_Model
from .forms import Musician
# Create your views here.

@method_decorator(login_required,name='dispatch')
class Create_Musician(CreateView):
    model= Musicians_Model
    form_class = Musician
    template_name = 'musician.html'
    success_url = reverse_lazy('home')

@method_decorator(login_required,name='dispatch')
class Edit_Musician(UpdateView):
    model= Musicians_Model
    form_class = Musician
    template_name = 'musician.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('home')

@method_decorator(login_required,name='dispatch')
class Delete_Musician(DeleteView):
    model=Musicians_Model
    template_name='delete.html'
    success_url=reverse_lazy('home')
    pk_url_kwarg='id'
