from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import ToDo, ToMeet

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