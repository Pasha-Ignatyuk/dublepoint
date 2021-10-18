"""Here you need to include url addresses of all applications of the project"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rm.urls')),
]
