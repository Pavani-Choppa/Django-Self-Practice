from django.urls import path,include
from myapp import views
urlpatterns = [

    path('',views.student_create,name='student_create')
]
