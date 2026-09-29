from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
# from .views import StudentListCreateAPIView, StudentRetrieveUpdateDeleteAPIView
from .views import StudentViewSet

router = DefaultRouter()
router.register('student', StudentViewSet, basename='student')
urlpatterns = [
    
    # path('students/',views.StudentAPI.as_view()),
    # path('students/<int:pk>/',views.StudentAPI.as_view())
    # path('student/', views.StudentListCreateAPIView.as_view(), name='student-list-create'),
    # path('student/<int:pk>/', views.StudentRetrieveUpdateDeleteAPIView.as_view(), name='student-retrieve-update-delete')
    path('', include(router.urls)),
]