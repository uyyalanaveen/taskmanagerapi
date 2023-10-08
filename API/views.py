from django.shortcuts import render
from .models import Task
from .serializer import task_serializer
from rest_framework import viewsets
# Create your views here.

class Taskview(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = task_serializer
