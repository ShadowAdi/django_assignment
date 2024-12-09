from django.urls import path
from . import views

urlpatterns = [
    path(route="todo/", view=views.get_tasks, name="GetTasks"),
    path(route="", view=views.IndexPage, name="Index"),
    path(route="todoCreate/", view=views.add_task, name="CreateTask"),
]
