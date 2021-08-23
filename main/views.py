from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *

def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

   

def tomeet(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, "meeting.html", {"tomeet_list": tomeet_list})
    
def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def habit(request):
    habit_list = Habit.objects.all()
    return render(request, "habits.html", {"habit_list": habit_list})

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)


def mark_todo(request, id):
    todo = ToDo.objects.get(id=id) 
    todo.is_favorite = True
    todo.save()
    return redirect(test) 

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id) 
    todo.is_favorite = False
    todo.save()
    return redirect(test)  