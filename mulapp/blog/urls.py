from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog_home),
    path('about/',views.blog_about),
]