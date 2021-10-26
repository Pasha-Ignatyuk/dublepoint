"""Module with Unit Tests"""
from decimal import Decimal
import datetime
from django.test import TestCase, RequestFactory
from . models import Department, Employee
from . views import add_new_dept
from django.contrib.auth import get_user_model

User = get_user_model()


class HRMTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        self.department = Department.objects.create(title="Test department")
        self.employee = Employee.objects.create(department=self.department, name="Konstantin", surname="Konstantinov",
                                                birthday=datetime.date(1982, 12, 14), salary=Decimal('10000.00'))
        self.employee = Employee.objects.create(department=self.department, name="Efim", surname="Efimov",
                                                birthday=datetime.date(1991, 6, 25), salary=Decimal('1000.00'))

    def test_average_salary(self):
        average_salary = self.department.average_salary
        self.assertEqual(average_salary, 5500.00)

    def test_add_new_dept(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user
        response = add_new_dept(request)
        self.assertEqual(response.status_code, 200)
