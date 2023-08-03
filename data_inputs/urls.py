# data_inputs/urls.py
from django.urls import path
from . import views

app_name = 'data_inputs'

urlpatterns = [
    path('', views.index, name='index'),
    path('loft_rental_form/', views.loft_rental_form_view, name='loft_rental_form'),
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]



