from django.urls import path

from .views import TodoViewSet
from rest_framework_bulk.routes import BulkRouter

router = BulkRouter()
router.register(r'', TodoViewSet, basename='todos')
urlpatterns = router.urls
