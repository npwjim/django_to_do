from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('list/', views.todo_list, name='list'),
]
