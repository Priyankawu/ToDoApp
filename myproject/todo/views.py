from todo.forms import TodoForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    context = {'todo_list' : todo_list, 'form': form}  # 'key': value pair - when u write 'form', you get form
    

    return render(request, 'todo/index.html', context)

#require_POST
def addToDo(request):
    form = TodoForm(request.POST)
    print(request.POST['text'])
    if(form.is_valid):
        new_todo = Todo(text = request.POST['text'])
        new_todo.save() #this adds to the database
    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')

def deleteComplete(request):
    #remove items marked as complete
    todo_list = Todo.objects
    todo_list.filter(complete__exact=True).delete()
    return redirect('index') 
    #for item in todo_list:
     #   if(item.completed == True):
      #      item.delete()
   
        

def completeTodo(request, todo_id):
    #get the item from the database
    todo = Todo.objects.get(pk=todo_id)
    #style a line across it
    todo.complete = True
    todo.save()
    return redirect('index')

    #return the new index.html