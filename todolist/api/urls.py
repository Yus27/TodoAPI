from django.urls import path

from .views import TodoViewSet
from rest_framework_bulk.routes import BulkRouter
from rest_framework import routers

router = BulkRouter()
router.register(r'', TodoViewSet, basename='todos')


urlpatterns = router.urls