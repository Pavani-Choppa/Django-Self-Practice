from django.urls import path
from api import views
from .views import StudentListCreateAPIView, StudentRetrieveUpdateDeleteAPIView
urlpatterns = [
    
    # path('students/',views.StudentAPI.as_view()),
    # path('students/<int:pk>/',views.StudentAPI.as_view())
    path('student/', views.StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('student/<int:pk>/', views.StudentRetrieveUpdateDeleteAPIView.as_view(), name='student-retrieve-update-delete')

]