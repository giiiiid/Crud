from django.db import models
import datetime
# Create your models here.
class Crud(models.Model):
    activity = models.CharField(max_length=200, default='', null=False)
    location = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.activity