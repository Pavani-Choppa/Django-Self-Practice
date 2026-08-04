from django.shortcuts import render

# Create your views here.
def app1_view(request):
    return render(request,'Template_app1/app1.html')

def app1_htm_view(request):
    return render(request,'Template_app1/app1_htm.html')