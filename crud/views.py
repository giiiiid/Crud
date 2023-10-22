from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CrudSerializer
from .forms import CrudForms
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
    return render(request, 'crud-index.html', context)


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



@api_view(['GET','POST','PUT','DELETE'])
def crudApi(request,activity):
    try:
        task = Crud.objects.get(activity=activity)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CrudSerializer(task)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CrudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = CrudSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return redirect('home')
    
    else:
        return render(request, 'crud-index.html')