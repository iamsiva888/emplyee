from django.contrib import admin
from django.urls import path
from employee_app import views

app_name = "employee_app"
urlpatterns = [
    path('', views.home, name='home'),
    path('employee_edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('employee_view/<int:pk>/', views.employee_view, name='employee_view'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee_register/', views.employee_register, name='employee_register'),
    path('employee_delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('employee_delete_confirm/<int:pk>/', views.employee_delete_confirm, name='employee_delete_confirm'),

]
