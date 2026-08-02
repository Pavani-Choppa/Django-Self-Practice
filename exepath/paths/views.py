from django.http import HttpResponse

# Create your views here.
def path_home(request,name,age):
    return HttpResponse(f"<h1 style='color: blue;'>Welcome {name} your age is {age}</h1>")

def repath_home(request,year):
    return HttpResponse(f"<h1 style='color: red;'>Welcome to the RePath Home Page! The year is {year}</h1>")

def kwarg_home(request,**kwargs):
    return HttpResponse(f"<h1 style='color: purple;'>Welcome to the Kwarg Home Page! The kwargs are {kwargs}</h1>")