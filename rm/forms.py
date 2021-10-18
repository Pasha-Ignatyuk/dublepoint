"""User-filled forms"""
from django import forms
from .models import Department


class DeptForm(forms.ModelForm):
    """Form for adding a new department"""
    class Meta:
        model = Department
        fields = ('title',)
