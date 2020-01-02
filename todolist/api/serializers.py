from rest_framework import serializers
from todolist.models import Todo
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin


class TodoSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'isCompleted', 'order', 'category')
        list_serializer_class = BulkListSerializer