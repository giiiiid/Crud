from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, unique=True, default='')
    email = models.EmailField(max_length=200, unique=True, default='')
    
    def __str__(self):
        return self.username

class Crud(models.Model):
    activity = models.CharField(max_length=200, default='', null=False)
    location = models.CharField(max_length=200, default='')
    profile = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.activity