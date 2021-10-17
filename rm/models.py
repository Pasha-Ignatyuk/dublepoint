from django.db import models
from django.db.models import Avg

class Department(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'

    @property
    def average_salary(self):
        average_salary = Employee.objects.filter(department=self).aggregate(Avg('salary'))
        if average_salary['salary__avg'] is None:
            return 'not applicable'
        return average_salary['salary__avg']


class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} {self.surname} salary {self.salary}'
