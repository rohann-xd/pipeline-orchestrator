from django.shortcuts import redirect, render
from .forms import TaskForm  # Import the TaskForm
from .models import Task

def task_list(request):
    """
    View function to display the list of tasks.
    """
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def create_task(request):
    """
    View function for creating a new task.
    """
    if request.method == 'POST':
        # If the form is submitted, process the form data
        form = TaskForm(request.POST)
        if form.is_valid():
            # If form data is valid, save the form and redirect to task list
            form.save()
            return redirect('task_list')
    else:
        # If the form is not submitted, display an empty form
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

def mark_completed(request, task_id):
    """
    View function to mark a task as completed.
    """
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    """
    View function to delete a task.
    """
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('task_list')
