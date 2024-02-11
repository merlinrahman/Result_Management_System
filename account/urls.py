from django.urls import path,include
from . import views

urlpatterns = [
    path('student_home/', views.student_home, name='student_home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('bit_login/', views.bit_login, name='bit_login'),
    path('comsci_login/', views.comsci_login, name='comsci_login'),
    path('masscom_login/', views.masscom_login, name='masscom_login'),
    
  
]