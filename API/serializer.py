from .models import Task
from rest_framework import serializers


class task_serializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        