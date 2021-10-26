"""url for each view with the corresponding html-template"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.departments_list, name='main_page'),
    path('<int:id>', views.department_detail, name='department_detail'),
    path('<int:id>', views.employee_detail, name='employee_detail'),
    path('new', views.add_new_dept, name='add_new_dept'),
]
