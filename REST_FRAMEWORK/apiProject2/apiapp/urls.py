
from django.urls import path
from apiapp import views

urlpatterns = [
    path('', views.Student_list,name='student_data'),
    
]