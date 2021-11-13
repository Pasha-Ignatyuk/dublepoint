"""View - is responsible for displaying information (visualization)"""
from django.shortcuts import render, get_object_or_404
from .models import Department, Employee
from .forms import DeptForm


def departments_list(request):
    """Presents a list of all departments on web page"""
    departments = Department.objects.all().order_by('title')
    return render(request, 'main_page.html', {'departments': departments})


def add_new_dept(request):
    """Form for adding a new department"""
    if request.method == "POST":
        form = DeptForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            departments = Department.objects.all().order_by('title')
            return render(request, 'main_page.html', {'departments': departments})
    else:
        form = DeptForm()
    return render(request, 'add_new_dept.html', {'form': form})


def department_detail(request, dept_id):
    """View for a specific department page. Accepts department's ID """
    deptartment = get_object_or_404(Department, id=dept_id)
    employee = Employee.objects.filter(department__id=dept_id)
    return render(request, 'department_detail.html', {'deptartment': deptartment,
                                                      'employee': employee})


def employee_detail(request, empl_id):
    """View for a specific employee page. Accepts employee's ID """
    employee = get_object_or_404(Employee, id=empl_id)
    return render(request, 'employee_detail.html', {'employee': employee})
