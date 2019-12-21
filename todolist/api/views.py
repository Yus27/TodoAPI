from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView, BulkModelViewSet

from todolist.models import Todo
from .serializers import TodoSerializer

class TodoViewSet(BulkModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def allow_bulk_destroy(self, qs, filtered):
        return True



