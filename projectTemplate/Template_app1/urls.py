from django.urls import path
from . import views

urlpatterns = [
    path('', views.app1_view),
    path('htm/', views.app1_htm_view),
]