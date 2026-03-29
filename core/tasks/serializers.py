from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'deadline', 'priority', 'status', 'user', 'created_at')
        read_only_fields = ('priority', 'user', 'created_at')
