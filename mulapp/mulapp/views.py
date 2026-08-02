
from django.http import HttpResponse


def fun1(request):
    return HttpResponse("<h1 style='color: green;'>Welcome to the Home Page!</h1>")