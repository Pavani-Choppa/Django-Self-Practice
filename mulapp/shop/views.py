from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def shop_home(request):
    return HttpResponse("<h1 style='color: purple;'>Welcome to the Shop Home Page!</h1>")

def shop_products(request):
    return HttpResponse("<h1 style='color: pink;'>Here are our products!</h1>")
