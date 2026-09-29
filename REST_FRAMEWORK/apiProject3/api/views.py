# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from .models import Student
# from .serializers import StudentSerializer


from rest_framework import generics,mixins
from .models import Student
from .serializers import StudentSerializer


# class StudentAPI(APIView):
#     def get(self,request,pk = None):
#         if pk:
#             try:
#                 student =Student.objects.get(id = pk)
#                 serializer = StudentSerializer(student)
#                 return Response(serializer.data,status=status.HTTP_200_OK)
#             except Student.DoesNotExist:
#                 return Response({"error":"Student Not Found"},status=status.HTTP_404_NOT_FOUND)
#         else:
#             student = Student.objects.all()
#             serializer = StudentSerializer(student,many=True)
#             return Response(serializer.data,status=status.HTTP_200_OK)

#     def post(self,request):
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def put(Self,request,pk):
#         try:
#             student = Student.objects.get(id = pk)
#         except Student.DoesNotExist:
#             return Response({"error":"Student NOT Found"},status=status.HTTP_404_NOT_FOUND)
#         serializer = StudentSerializer(student,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#     def delete(self,request,pk):
#         try:
#             student = Student.objects.get(id = pk)
#             student.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

#         except Student.DoesNotExist:
#             return Response({"error":"Student NOT Found"},status=status.HTTP_404_NOT_FOUND)
        



# Generic API View

class StudentListCreateAPIView(generics.ListCreateAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #To Return List of Student
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    # to create a new student
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StudentRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # To retrieve a student by ID
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    # To update a student by ID
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    # To delete a student by ID
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

