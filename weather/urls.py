from django.urls import path
from . import views

urlpatterns = [
    path('art/', views.index, name='index'),
    path('delete/<str:city_name>/', views.delete_city, name='delete_city'),
]