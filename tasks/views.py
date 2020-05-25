from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    tk = task.objects.all()
    form = taskForm()
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,('New Items has been added to the list'))
        return redirect('/')
    return render(request,'tasks/index.html',{'tk':tk ,'form':form})


def updateTask(request,pk):
    tas = task.objects.get(id=pk)
    form = taskForm(instance=tas)
    if request.method == 'POST':
        form = taskForm(request.POST , instance=tas)
        if form.is_valid():
            form.save()
            messages.success(request,('An Item in the list has been updated'))
            return redirect('/')
    return render(request, 'tasks/update_task.html',{'form':form})


def deleteTask(request,pk):
    item = task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request,('Items has been removed from the list'))
        return redirect('/')
    return render(request, 'tasks/delete.html',{'item':item})