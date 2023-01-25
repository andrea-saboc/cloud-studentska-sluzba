from django.db import models
from datetime import date

# Create your models here.

TITLE_CHOICES = (
    ("Research assistant professor", "Research assistant professor"),
    ("Research associate professor", "Research associate professor"),
    ("Research professor", "Research professor")
)

class Professor(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=100)
    jmbg = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images')
    birthDate = models.DateField(default=date.today, blank=True)
    title = models.CharField(max_length=50, choices=TITLE_CHOICES, default="Research professor", blank=True)


    def __str__(self) -> str:
        return f'{self.title} - {self.name} - {self.surname}'

class Student(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=100)
    jmbg = models.CharField(max_length=20)
    birthDate = models.DateField(default=date.today, blank=True)
    indexNumber = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    

    def __str__(self) -> str:
        return f'{self.name} - {self.surname} - {self.indexNumber}'