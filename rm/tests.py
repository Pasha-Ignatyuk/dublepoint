"""Module with Unit Tests"""
from decimal import Decimal
import datetime
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from .models import Department, Employee
from .views import add_new_dept

User = get_user_model()


class HRMTestCase(TestCase):
    """Instances of the TestCase class represent the logical test units in the unittest universe.
    This class is intended to be used as a base class, with specific tests being implemented by concrete subclasses.
    This class implements the interface needed by the test runner to allow it to drive the tests, and methods that the
    test code can use to check for and report various kinds of failure."""
    def setUp(self):
        """Method called to prepare the test fixture. This is called immediately before calling the test method.
        Preliminary creation of objects of classes Department and Employee for subsequent testing"""
        self.user = User.objects.create(username='testuser', password='password')
        self.department = Department.objects.create(title="Test department")
        self.employee = Employee.objects.create(department=self.department, name="Konstantin", surname="Konstantinov",
                                                birthday=datetime.date(1982, 12, 14), salary=Decimal('10000.00'))
        self.employee = Employee.objects.create(department=self.department, name="Efim", surname="Efimov",
                                                birthday=datetime.date(1991, 6, 25), salary=Decimal('1000.00'))

    def test_average_salary(self):
        """Checking the calculation of the average salary of two employees of the department, named "Test
        department" """
        average_salary = self.department.average_salary
        self.assertEqual(average_salary, 5500.00)

    def test_add_new_dept(self):
        """Checking the success of adding a department through the form"""
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user
        response = add_new_dept(request)
        self.assertEqual(response.status_code, 200)
