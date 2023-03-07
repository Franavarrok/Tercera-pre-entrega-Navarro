from django.db import models

# Create your models here.
class School (models.Model):

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.IntegerField()
    gmail = models.EmailField()

class Professor (models.Model):

    name = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.IntegerField()
    gmail = models.EmailField()

class Student (models.Model):

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)   
    grade = models.IntegerField()
    age = models.IntegerField()
    phone = models.IntegerField()
    gmail = models.EmailField()


