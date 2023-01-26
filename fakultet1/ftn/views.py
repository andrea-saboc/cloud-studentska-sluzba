from django.shortcuts import render, redirect
from django.http import HttpResponse
from PIL import Image
import json
import requests

from .models import Professor, Student
from .forms import RegistrationStudentForm, RegistrationProfessorForm


# Create your views here.

def homepage(request):
    return render(request, 'ftn/homepage.html')


def register_professor(request):
    if request.method == 'GET':
        registration_form = RegistrationProfessorForm()
        return render(request, 'ftn/registerprofessor.html', {
            "form": registration_form
        })

    elif request.method == 'POST':
        print("here")
        registration_form = RegistrationProfessorForm(request.POST, request.FILES)

        if registration_form.is_valid():
            professor = registration_form.cleaned_data
            pr = Professor(
                title=professor['title'],
                name=professor['name'],
                surname=professor['surname'],
                jmbg=professor['jmbg'],
                birthDate=professor['birthDate'],
                image=professor['image']
            )
            prJSON = {
                "name": "%s" % professor['name'],
                "surname": "%s" % professor['surname'],
                "jmbg": "%s" % professor['jmbg'],
            }
            pr.save()

            response = requests.post('http://nginx:80/professors',
                                     headers={'Content-Type': 'application/json'}, json=prJSON)
            print("response before trying")
            print(response)
            try:
                # print("\nStatus code" + response.status_code)
                if (response.status_code == 200):
                    pr.save()
                    response="Professor is registered!"
                    registration_form = RegistrationStudentForm()
                elif (response.status_code == 409):
                    response="Already exists!"
                else:
                    response="Error!"
            finally:
                return HttpResponse(response)


def index(request):
    sudents = Student.objects.all
    if request.method == 'GET':
        registration_form = RegistrationStudentForm()
        return render(request, 'ftn/registerstudent.html', {
            "form": registration_form
        })
    elif request.method == 'POST':
        registration_form = RegistrationStudentForm(request.POST, request.FILES)

        if registration_form.is_valid():
            student = registration_form.cleaned_data
            print("cleaned data:\n")
            # print(student['image'].image)
            st = Student(
                name=student['name'],
                surname=student['surname'],
                jmbg=student['jmbg'],
                indexNumber=student['indexNumber'],
                image=student['image'],
                birthDate=student['birthDate'],
            )
            print(st)
            stJSON = {
                "name": "%s" % student['name'],
                "surname": "%s" % student['surname'],
                "jmbg": "%s" % student['jmbg'],
            }
            response = requests.post('http://nginx:80/students',
                                     headers={'Content-Type': 'application/json'}, json=stJSON)
            print("response before trying")
            print(response)
            try:
                if (response.status_code == 200):
                    st.save()
                    response ="Student is registered!"
                elif (response.status_code == 409):
                    response = "Already exists!"
                else:
                    response ="Error!"

                return HttpResponse(response)
            finally:
                return HttpResponse(response)
