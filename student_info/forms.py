from django import forms

from .models import Student

class StudentForm(forms.ModelForm):   #Modelform to get the input from the user and feed it directly into the database

    class Meta:
        model = Student
        fields = ('name', 'age', 'gender')
