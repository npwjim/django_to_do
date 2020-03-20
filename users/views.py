from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views


from .forms import CustomUserCreationForm


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'


class LogoutView(auth_views.LogoutView):
    next_page = '/'


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'
