from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.CharField(primary_key=True ,max_length=10)
    branch = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    section = models.CharField(max_length=10)
