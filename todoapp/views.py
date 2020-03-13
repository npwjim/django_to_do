from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = 'todoapp/login.html'


class LogoutView(auth_views.LogoutView):
    next_page = '/todo/'


def index(request):
    return render(request, 'todoapp/index.html')


@login_required
def todo_list(request):
    return HttpResponse("Hi, this is your to-do list.")


# def login(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect('/index/')
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         auth.login(request, user)
#         return HttpResponseRedirect('/index/')
#     else:
#         return render(request, 'todoapp/login.html', locals())
#
#
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect('/index/')
