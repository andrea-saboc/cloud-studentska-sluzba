from django import forms
from .models import Student, Professor, TITLE_CHOICES

class RegistrationStudentForm(forms.Form):
    #class Meta:
        model =Student
        name = forms.CharField(label="Student's name", max_length=60)
        surname = forms.CharField(label="Student's surname", max_length=100)
        jmbg = forms.CharField(label="JMBG", max_length=20)
        birthDate = forms.DateField(label="birthDate", required=False)
        image = forms.ImageField(label="image", required=False, initial='profile.jpg')
        indexNumber = forms.CharField(label="Index number", max_length=50)

class RegistrationProfessorForm(forms.Form):
    model=Professor
    title = forms.ChoiceField(label="title",choices=TITLE_CHOICES)
    name = forms.CharField(label="Professor's name", max_length=60)
    surname = forms.CharField(label="Professor's surname", max_length=100)
    jmbg = forms.CharField(label="JMBG", max_length=20)
    birthDate = forms.DateField(label="birthDate", required=False)
    image = forms.ImageField(label="image", required=False, initial='profile.jpg')
