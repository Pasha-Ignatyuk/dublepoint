from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.departments_list, name='main_page'),
    path('<int:pk>', views.department_detail, name='department_detail'),
    path('new', views.add_new_dept, name='add_new_dept'),
]