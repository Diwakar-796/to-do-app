from django.shortcuts import render, redirect
from .models import Task, Category, PRIORITY
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def home(request):
    tasks = []
    task_done = 0
    categories = Category.objects.all()

    tasks = Task.objects.all().order_by('-priority')
    try:
        task_done = tasks.filter(is_done=True)
    except:
        task_done = 0

    context = {
        'tasks': tasks,
        'categories': categories,
        'task_done': task_done,
        'priorities': PRIORITY,
    }

    return render(request, 'core/home.html', context)

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('add-task')
        category_id = request.POST.get('category')
        priority = request.POST.get('priority')
        category = None

        if category_id:
            category = Category.objects.get(id=category_id)

        if title:
            Task.objects.create(
                title=title,
                category=category,
                priority = priority
            )
            messages.success(request, "Task added successfully.")
        else:
            messages.warning(request, "Task can't be empty.")
        return redirect('home')
    return redirect('home')

def task_detail(request, id):
    task = Task.objects.get(id=id)
    categories = Category.objects.all()

    context = {
        'task':task, 
        'categories':categories,
        'priorities':PRIORITY,
    }

    return render(request, 'core/task_detail.html', context)

def del_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request, "Task deleted successfully.")
    return redirect('home')

def done_task(request, id):
    task = Task.objects.get(id=id)
    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True

    task.save()
    messages.success(request, "Task updated successfully.")
    return redirect('home')

def edit_task(request, id):
    if request.method == "POST":
        task = Task.objects.get(id=id)
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        priority = request.POST.get('priority')
        category = None

        if category_id:
            category = Category.objects.get(id=category_id)

        if title:
            task.title=title
            task.category=category
            task.priority = priority
            task.save()
            messages.success(request, "Task updated successfully.")
        else:
            messages.error(request, "Task can't be empty.")
    return redirect('home')

def filter_task(request):
    if request.method == "POST":
        category_id = request.POST.get("category")
        level = request.POST.get("level")

        if category_id == "All Tasks":
            task = Task.objects.all().order_by('-level')
        else:
            task = Task.objects.filter(category_id=category_id).order_by('-level')

        if level == "All Tasks":
            tasks = task.all()
        else:
            tasks = task.filter(level=level)

        return render(request, "core/home.html", {"tasks": tasks})

    return redirect("home")

def search_task(request):
    query = request.GET.get('query')
    tasks = Task.objects.filter(
        Q(title__icontains=query) |
        Q(category__title__icontains=query) |
        Q(priority__icontains=query)
    )
    return render(request, 'core/home.html', {'tasks': tasks})

def add_category(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Category.objects.create(title=title)
            messages.success(request, "Category added successfully.")
        else:
            messages.warning(request, "Category can't be empty.")
        return redirect('home')
    return redirect('home')
