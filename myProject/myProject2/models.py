from django.db import models

# Create your models here.

class student(models.model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    cgpa=models.IntegerField()

