from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerailizer
from rest_framework.response import Response

@api_view(['GET'])
def Student_list(request):
    students = Student.objects.all()
    serializer = StudentSerailizer(students, many = True)
    return Response(serializer.data)