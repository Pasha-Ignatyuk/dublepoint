from django.shortcuts import render, get_object_or_404
from .models import Department
from .forms import DeptForm


def departments_list(request):
    departments = Department.objects.all().order_by('title')
    return render(request, 'main_page.html', {'departments': departments})


def add_new_dept(request):
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


def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'department_detail.html', locals())
