from django.urls import path,include
from .import views

urlpatterns = [
     path('register/',views.RegisterView.as_view(), name='register'),
     path('logIn/',views.UserLogin.as_view(), name='logIn'),
     path('LogOut/',views.CustomLogoutView.as_view(),name='LogOut'),
]