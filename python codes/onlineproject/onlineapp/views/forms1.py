from onlineapp.models import *
from django import  forms


class CollegeForm(forms.ModelForm):
    class Meta:
        model=College
        exclude=['id']


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        exclude=['id','college']
""" widgets={
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter student name'}),
            'email':forms.EmailField(attrs={'class':'form-control','placeholder':'Enter student name'}),
}"""

class MockForm(forms.ModelForm):
    class Meta:
        model = MockTest1
        exclude = ['id','student','total']

