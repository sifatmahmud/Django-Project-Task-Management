from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task

# Create your views here.

def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

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
    # retrive all data from tasks model
    tasks = Task.objects.all()

    #retrive a specific task
    task_3 = Task.objects.get(pk=1)

    # Fetch the first task
    first_task = Task.objects.first()
    return render(request, "show_task.html", {"tasks":tasks, "task3":task_3, "first_task":first_task})