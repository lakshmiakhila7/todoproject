from django.shortcuts import render, redirect
from .models import Task

def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('home')  # Redirect to avoid form resubmission

    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.completed = 'completed' in request.POST
        task.save()
    return redirect('home')
