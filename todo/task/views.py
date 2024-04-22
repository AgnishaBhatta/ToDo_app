from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import data
from .forms import dataForm
def index(request):
    data1 = data.objects.all()
    form = dataForm()
    if request.method == 'POST':
        form = dataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'data':data1, 'form':form}
    return render(request, 'task/list.html', context)

def updateTask(request, pk):
    gdata = data.objects.get(id=pk)
    form=dataForm(instance=gdata) 
    if request.method == 'POST':
        form = dataForm(request.POST, instance=gdata)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'form':form}  
    return render(request, 'task/update.html', context)

def deleteTask(request, pk):
    item = data.objects.get(id=pk)
    context={'item':item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'task/delete.html',context)
   

# Create your views here.
