from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('doctor_profile/',views.doctor_profile,name='doctor_profile'),
    path('registration/',views.register_patient,name='registration'),
    path('doctor_list/',views.doctor_list,name='doctor_list'),
    path('delete/<int:id>/',views.delete,name='delete-data'),
    path('update/<int:id>',views.update,name='update-data'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update_profile, name='update_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('pay/', views.initiate_payment, name='pay'),
    path('payment-response/', views.payment_response, name='payment_response'),
]
