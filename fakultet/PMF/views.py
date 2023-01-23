from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
import  requests

from .models import Professor, Student
from .forms import RegistrationStudentForm, RegistrationProfessorForm

# Create your views here.

def homepage(request):
    return render(request, 'PMF/homepage.html')

def register_professor(request):
    if request.method == 'GET':
        registration_form = RegistrationProfessorForm()
        return render(request, 'PMF/register-professor.html', {
            "form": registration_form
        })

def index(request):
    sudents = Student.objects.all
    if request.method == 'GET':
        registration_form = RegistrationStudentForm()
        return render(request, 'PMF/index.html', {
            "form" : registration_form
        })
    elif request.method=='POST':
        registration_form = RegistrationStudentForm(request.POST)
        
        if registration_form.is_valid():
            student = registration_form.cleaned_data
            st = Student(
                name = student['name'],
                surname = student['surname'],
                jmbg = student['jmbg'],
                #indexNumber = student['indexNumber']
            )
            stJSON = {
                "name" : "%s" % student['name'],
                "surname" : "%s" % student['surname'],
                "jmbg" : "%s" % student['jmbg'],
            }

            try:
                response = requests.post('http://localhost:8080/students',
                                        headers={'Content-Type': 'application/json'}, json = stJSON)
                if(response.status_code == 200):
                    st.save()
                    print("Student is registered!")
                    registration_form = RegistrationStudentForm()
                elif(response.status_code==409):
                    print("Already exists!")
                else:
                    print("Error!")


                return render(request, 'PMF/index.html', {
                    "form" : registration_form
                })
            except:
                return HttpResponse(response)
