from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='doctor_home'),
    path('create/', views.doctor_create, name='doctor_create'),
    path('update/<int:pk>/', views.doctor_update, name='doctor_update'),
    path('delete/<int:pk>/', views.doctor_delete, name='doctor_delete'),
]
