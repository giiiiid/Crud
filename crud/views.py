from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CrudSerializer
from .forms import CrudForms, SongForms
from .models import Crud
# Create your views here.


# function to display all tasks
def home(request):
    if request.method == 'POST':
        activity = request.POST['task']
        location = request.POST['location']

        task = Crud.objects.create(activity=activity, location=location)
        task.save()
        return redirect('home')
    
    tasks = Crud.objects.all()
    context = {'tasks':tasks}
    return render(request, 'index.html', context)


# function to view a task - detailview
def detail(request, activity):
    task = Crud.objects.get(activity=activity)
    context = {'task':task}
    return render(request, 'crud-detail.html', context)


# function to update a task
def update(request, activity):
    task = Crud.objects.get(activity=activity)

    forms = CrudForms()
    if request.method == 'POST':
        forms = CrudForms(request.POST, instance=task)
        if forms.is_valid():
            forms.save()
        return redirect('home')

    context = {'forms':forms, 'task':task}
    return render(request, 'crud-update.html', context)


# function to delete a task after completion
def done(request, activity):
    task = Crud.objects.get(activity=activity)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    context = {'task':task}
    return render(request, 'crud-done.html', context)


# function to delete a task
def delete(request, activity):
    task = Crud.objects.get(activity=activity)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    context = {'task':task}
    return render(request, 'crud-delete.html', context)


# function for the API
@api_view(['GET'])
def crudApi(request):
    task = Crud.objects.all()
    serializer = CrudSerializer(task, many=True)
    return JsonResponse(serializer.data, safe=False)