from django.db import models
import datetime
# Create your models here.
class Crud(models.Model):
    activity = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200, default='')
    # time = models.TimeField(blank=True, null=True, default=datetime.time)

    def __str__(self):
        return self.activity