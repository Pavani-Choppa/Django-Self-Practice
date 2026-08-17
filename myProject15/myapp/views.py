from django.shortcuts import get_object_or_404, render
from .models import Student
from .forms import StudentForm
# Create your views here.

def student_create(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'student_success.html')
    return render(request,'student_form.html',{'form':form})

def student_list(request):
    students = Student.objects.all()
    return render(request,'student_list.html',{'students':students})

def student_detail(request,pk):
    student = get_object_or_404(Student,pk=pk)
    return render(request,'student_detail.html',{'student':student})


