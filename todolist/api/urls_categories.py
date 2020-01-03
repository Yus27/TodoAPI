from django.urls import path

from .views import CategoriesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', CategoriesViewSet, basename='categories')


urlpatterns = router.urls
