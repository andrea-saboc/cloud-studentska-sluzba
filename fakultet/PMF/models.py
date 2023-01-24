from django.db import models
from datetime import date

# Create your models here.

class Professor(models.Model):
    class Title(models.TextChoices):
        RESEARCH_ASSISTANT_PROFESSOR = 'RAS', ('Research assistant professor')
        RESEASRCH_ASSOCIATE_PROFESSOR = 'RATP', ('Research associate professor')
        RESEARCH_PROFESSOR = 'RP', ('Research professor')
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=100)
    jmbg = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images')
    birthDate = models.DateField(default=date.today, blank=True)


    def __str__(self) -> str:
        return f'{self.Title} - {self.name} - {self.surname}'

class Student(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=100)
    jmbg = models.CharField(max_length=20)
    birthDate = models.DateField(default=date.today, blank=True)
    indexNumber = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    

    def __str__(self) -> str:
        return f'{self.name} - {self.surname} - {self.indexNumber}'