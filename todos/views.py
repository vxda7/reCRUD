from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    due_date = request.GET.get('duedate')
    todo = Todo()
    todo.title = title
    todo.due_date = due_date
    todo.save()

    return redirect('/todos/')

