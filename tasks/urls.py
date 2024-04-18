from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # URL pattern for the task list
    path('create/', views.create_task, name='create_task'),  # URL pattern for creating a new task
    path('mark-completed/<int:task_id>/', views.mark_completed, name='mark_completed'),  # URL pattern for marking a task as completed
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),  # URL pattern for deleting a task
]
