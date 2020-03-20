from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'todoapp/index.html')


@login_required
def todo_list(request):
    return HttpResponse("Hi, this is your to-do list.")


# class LoginView(auth_views.LoginView):
#     template_name = 'todoapp/login.html'
#
#
# class LogoutView(auth_views.LogoutView):
#     next_page = '/todo/'
#
#
# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return HttpResponseRedirect('/todo/accounts/login/')
#     else:
#         form = UserCreationForm(request.POST)
#     return render(request, 'todoapp/register.html', locals())
