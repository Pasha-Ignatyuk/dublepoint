"""Module for registration of models"""
from django.contrib import admin
from rm.models import Department, Employee

admin.site.register(Department)
admin.site.register(Employee)
