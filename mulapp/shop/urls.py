from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop_home),
    path('products/',views.shop_products)
]