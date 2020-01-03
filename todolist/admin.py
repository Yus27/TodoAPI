from django.contrib import admin

from .models import Todo, Category
# from rest_framework.authtoken.models import Token

admin.site.register(Todo)
admin.site.register(Category)
# admin.site.register(Token)
