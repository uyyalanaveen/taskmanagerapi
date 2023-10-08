from django.db import models
from datetime import datetime

class Task(models.Model):
    Title = models.CharField(max_length=50,null=False,blank=False)
    Description = models.TextField()
    Completed = models.BooleanField(default=False)
    Date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title