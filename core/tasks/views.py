from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from services.priority_calculator import calculate_priority

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # User isolation: only return tasks for the authenticated user
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        
        # Filtering functionality
        status = self.request.query_params.get('status', None)
        priority = self.request.query_params.get('priority', None)
        
        if status:
            queryset = queryset.filter(status__iexact=status)
        if priority:
            queryset = queryset.filter(priority__iexact=priority)
            
        return queryset.order_by('deadline')

    def perform_create(self, serializer):
        # Auto-calculate priority based on deadline
        deadline = serializer.validated_data.get('deadline')
        calculated_priority = calculate_priority(deadline)
        # Assign user and calculated priority
        serializer.save(user=self.request.user, priority=calculated_priority)

    def perform_update(self, serializer):
        # Recalculate priority if deadline changes
        deadline = serializer.validated_data.get('deadline')
        # If deadline is not provided in a partial update, fetch existing
        if not deadline and self.get_object():
            deadline = self.get_object().deadline
            
        calculated_priority = calculate_priority(deadline)
        serializer.save(priority=calculated_priority)
