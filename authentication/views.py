from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .import forms


class RegisterView(FormView):
    template_name = 'Register.html'
    form_class = forms.RegistrationFrom
    success_url = reverse_lazy('home')  # Assuming 'register' is the name of the URL pattern

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account Created Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'invalid Information ?')
        return self.render_to_response(self.get_context_data(form=form))

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(form=self.get_form()))

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Registration'
        return context



class UserLogin(LoginView):
    template_name='Register.html'

    
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self,form):
        messages.success(self.request,"logged in successfully")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request,"logged in information incorrect ?")
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'login'
        return context

@method_decorator(login_required,name='dispatch')
class CustomLogoutView(View):
    def get(self, request,):
        logout(request)
        return redirect('home')
# path('register/', RegisterView.as_view(), name='register'),
