from django import forms
from first_app import models

class Student(forms.ModelForm):
    class Meta:
        model= models.StudentForm
        fields="__all__"