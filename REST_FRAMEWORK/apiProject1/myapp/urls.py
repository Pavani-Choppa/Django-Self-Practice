from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.Student_list,name='student-list')
]
