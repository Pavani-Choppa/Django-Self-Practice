from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField()

    def __str__(self):
        return str(self.city)

class Profile(models.Model):
    bio = models.TextField()
    location = models.CharField(max_length=100)
    dob = models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.dob)