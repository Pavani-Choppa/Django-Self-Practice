from django.urls import path
from . import views

urlpatterns = [
    path('',views.app2_fun),
    path('html/',views.app2_html_fun),
]