from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    emmail = models.EmailField(max_length=255, unique=True)

