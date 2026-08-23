from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerailizer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def Student_list(request):
    students = Student.objects.all()
    serializer = StudentSerailizer(students, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def Add_Student(request):
    serializer = StudentSerailizer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


@api_view(['PUT','PATCH'])
def update_student(request,pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"error":"Student Not Found"},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = StudentSerailizer(student,data = request.data,partial = True)
    else:
        serializer = StudentSerailizer(student,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request,pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"error":"Student NOT FOUND"},status=status.HTTP_404_NOT_FOUND)

    student.delete()
    return Response({"message":"Student  Deleted Sucessfully."},status=status.HTTP_204_NO_CONTENT)



