from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app_fun(request):
    return HttpResponse("<h1 style='color: blue;'>Hello, This is my first Django app.</h1>")

def app_fun2(request):
    return HttpResponse("<h1 style='color: yellow;'>Hello, This is my second Django app.</h1>")

def app_fun3(request):
    return HttpResponse("<h1 style='color: pink;'>Hello, This is my third Django app.</h1>")