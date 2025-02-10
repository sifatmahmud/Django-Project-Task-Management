from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg

# Create your views here.

def manager_dashboard(request):

    type = request.GET.get('type', 'all')
    # print(type)

    counts = Task.objects.aggregate(
        total=Count('id'), 
        completed=Count('id', filter=Q(status= 'COMPLETED')),
        in_progress=Count('id', filter=Q(status= 'IN_PROGRESS')),
        pending=Count('id', filter=Q(status= 'PENDING'))
        )
    
    # Retriving task data
    base_query = Task.objects.select_related('details').prefetch_related('assigned_to')

    if type == 'completed':
        tasks = base_query.filter(status='COMPLETED')
    elif type == 'in-progress':
        tasks = base_query.filter(status='IN_PROGRESS')
    elif type == 'pending':
        tasks = base_query.filter(status='PENDING')
    elif type == 'all':
        tasks = base_query.all()

    context = {
        "tasks": tasks,
        "counts": counts
    }

    return render(request, "dashboard/manager-dashboard.html", context)

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    context = {
        "names":["Mahmud", "Ahmed", "John"],
        "age":23
    }
    return render(request, 'test.html', context)


def create_task(request):
    # employees = Employee.objects.all()
    form = TaskModelForm() # For GET

    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            ''' For Model Form Data '''
            form.save()

            return render(request, 'task_form.html', {"form":form, "message": "task added successfully"})

    context = {"form": form}
    return render(request, "task_form.html", context)


def view_task(request):
    # task_count = Task.objects.aggregate(num_task=Count('id'))
    projects = Project.objects.annotate(num_task=Count('task')).order_by('num_task')
    return render(request, "show_task.html", {"projects":projects})