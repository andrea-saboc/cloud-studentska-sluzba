from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Professor, Student
from .forms import RegistrationStudentForm, RegistrationProfessorForm

# Create your views here.

def index(request):
    sudents = Student.objects.all
    if request.method == 'GET':
        registration_form = RegistrationStudentForm()
        return render(request, 'PMF/index.html', {
            "form" : registration_form
        })
    else:
        registration_form = RegistrationStudentForm(request.POST)
        
        if registration_form.is_valid():
            student = registration_form.cleaned_data

            st = Student(
                name = student['name'],
                surname = student['surname'],
                jmbg = student['jmbg'],
                indexNumber = student['indexNumber']
            )
            st.save()

            return render(request, 'PMF/index.html', {
                "form" : registration_form
            })
