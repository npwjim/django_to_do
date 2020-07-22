from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
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
    completed_items = Todo.objects.filter(user=request.user, done=True).order_by('-added_date')
    return render(request, 'todoapp/list.html', {
        "todo_items": todo_items,
        "completed_times": completed_items,
    })


def add_todo(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    if request.POST["content"].split():
        Todo.objects.create(user=request.user, text=request.POST["content"])
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


@login_required
def search_todo(request):
    if request.GET:  # what if access search view via GET method
        query_string = request.GET["search"]
        found_tasks = set()
        if query_string.split():  # what if the content in queryText makes sense
            query_string_list = query_string.split()
            for string in query_string_list:
                for result in Todo.objects.filter(text__icontains=string):
                    found_tasks.add(result)
        else:  # if the content does not make sense, list all tasks
            found_tasks = Todo.objects.all()
        return render(request, 'todoapp/result.html', {
            "query_string": query_string,
            "found_tasks": found_tasks,
        })
    else:
        return HttpResponseRedirect(reverse("todoapp:list"))
