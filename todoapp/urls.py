from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.todo_list, name='list'),
    path('add/', views.add_todo, name='add'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete'),
    path('finish/<int:todo_id>/', views.finish_todo, name='finish'),
]
