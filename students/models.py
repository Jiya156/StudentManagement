from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Roll_Number = models.CharField(max_length=50)
    Course = models.CharField(max_length=50)
    Semester = models.IntegerField()
    Batch = models.IntegerField()

# Create your models here.
