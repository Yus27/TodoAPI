from rest_framework import serializers
from todolist.models import Todo, Category
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin


class TodoSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'isCompleted', 'lastChangeDateTime', 'order', 'category')
        list_serializer_class = BulkListSerializer


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'catTitle')