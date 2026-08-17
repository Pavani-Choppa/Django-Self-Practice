from django.urls import path,include
from myapp import views
urlpatterns = [
    path('',views.student_create,name='student_create'),
    path('list/',views.student_list,name='student_list'),
    path('details/<int:pk>',views.student_detail,name='student_detail')
]
