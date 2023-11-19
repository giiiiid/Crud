from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Crud, Profile
from .serializers import CrudSerializer
from .forms import CrudForms, SignUpForms, LoginForms

# Create your views here.


# function to display all tasks
def index(request):
    return render(request, 'index.html')

def user_home(request):
    
    if request.method == 'POST':
        activity = request.POST['task']
        location = request.POST['location']

        task = Crud.objects.create(activity=activity, location=location)
        task.save()
        return redirect('home')
    
    tasks = Crud.objects.all()
    context = {'tasks':tasks}
    return render(request, 'user-home.html')
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

def search(request):
    if request.method == 'POST':
        searched = request.POST['search']
        lookup = Q(activity__icontains=searched) | Q(location__icontains=searched)
        searched_tasks = Crud.objects.filter(lookup)
        
        if searched_tasks.exists():
            context = {'searched_tasks':searched_tasks, 'searched':searched}
        else:
            messages.info(request, f'{searched} does not exist')
            context = {'searched':searched}
            return redirect('home')
        return render(request, 'search-task.html', context)
    else:
        return render(request, 'search-task.html')


def sign_up(request):
    # forms = SignUpForms()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
            # username = forms.cleaned_data['username']
            # email = forms.cleaned_data['email']
            # password = forms.cleaned_data['password1']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                Profile.objects.create(user=user)
                messages.success(request, f'{username}, your account has been created')
        else:
            messages.info(request, 'Passwords do not match')
        # return redirect('login')
    context = {}
    return render(request, 'signup.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'login.html', context)










# function for the API
@api_view(['GET'])
def crudApi(request):
    task = Crud.objects.all()
    serializer = CrudSerializer(task, many=True)
    return JsonResponse(serializer.data, safe=False)