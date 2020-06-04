from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template.defaultfilters import length
from django.utils import timezone
from django.urls import reverse

from .models import Todo


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("todoapp:list"))
    else:
        return render(request, 'todoapp/index.html')


@login_required
def todo_list(request):
    todo_items = Todo.objects.filter(user=request.user, done=False).order_by('-added_date')
    finished_items = Todo.objects.filter(user=request.user, done=True).order_by('-added_date')
    return render(request, 'todoapp/list.html', {
        "todo_items": todo_items,
        "finished_times": finished_items,
    })


def add_todo(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    content = request.POST["content"]
    created_obj = Todo.objects.create(user=request.user, text=content)
    length_of_todos = Todo.objects.all().count()
    return HttpResponseRedirect(reverse("todoapp:list"))


def delete_todo(request, todo_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect(reverse("todoapp:list"))


def finish_todo(request, todo_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    finished_todo = Todo.objects.get(id=todo_id)
    finished_todo.done = True
    finished_todo.save()
    return HttpResponseRedirect(reverse("todoapp:list"))


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
