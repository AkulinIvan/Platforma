from django.urls import path
from companies import views

app_name = 'companies'

urlpatterns = [
    path('', views.company, name='company'),
    path('create_company/', views.create_company, name='create_company'),
    
]