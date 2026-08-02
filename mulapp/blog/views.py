from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog_home(request):
    return HttpResponse("<h1 style='color: blue;'>Welcome to the Blog Home Page!</h1>")

def blog_about(request):
    return HttpResponse("<h1 style='color: green;'>About the Blog</h1><p>This is a simple blog application built with Django.</p>")