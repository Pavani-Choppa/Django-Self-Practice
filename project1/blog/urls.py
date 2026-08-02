
from sys import path
from django.contrib import admin
from blog import views
from django.urls import path

urlpatterns = [
        # path('admin/', admin.site.urls),
        path('blog/',views.app_fun),
        path('fun2/',views.app_fun2),
        path('fun3/',views.app_fun3),
        
]