
from django.urls import path
from apiapp import views

urlpatterns = [
    path('', views.Student_list,name='student_data'),
    path('add/',views.Add_Student,name='add_student'),
    path('update/<int:pk>/',views.update_student,name='update_student'),
    path('delete/<int:pk>/',views.delete_student,name='delete_student'),

    
    
]