from django.urls import path,re_path
from . import views
urlpatterns = [
    path('path/<str:name>/<int:age>/',views.path_home),
    re_path(r'^repath/(?P<year>[0-9]{4})/$',views.repath_home),
    path('kwarg/<str:key>/<int:value>/',views.kwarg_home),
]