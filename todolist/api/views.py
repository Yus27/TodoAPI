from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView, BulkModelViewSet


from todolist.models import Todo, Category
from .serializers import TodoSerializer, CategoriesSerializer


class TodoViewSet(BulkModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def allow_bulk_destroy(self, qs, filtered):
        return True


class CategoriesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategoriesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        cat = get_object_or_404(queryset, pk=pk)
        serializer = CategoriesSerializer(cat)
        return Response(serializer.data)


# class CategoriesList(generics.ListAPIView):
#     serializer_class = CategoriesSerializer
#     queryset = Category.objects.all()

#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = CategoriesSerializer(queryset, many=True)
#         return Response(serializer.data)



