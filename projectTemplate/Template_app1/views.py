from django.shortcuts import render

# Create your views here.
def app1_view(request):
    return render(request,'Template_app1/app1.html')