from django import forms
from .models import Department


class DeptForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('title',)
