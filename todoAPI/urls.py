
from django.contrib import admin
from django.urls import path, include
# from rest_framework.authtoken import views 

urlpatterns = [
    # path('api/auth/', include('rest_framework.urls')),    
    path('admin/', admin.site.urls),
    path('api/', include('todolist.api.urls')),
    path('categories/', include('todolist.api.urls_categories')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
