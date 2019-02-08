from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    """Custom todo admin form
    """
    class Meta:
        model = Todo
        exclude = ['user',]