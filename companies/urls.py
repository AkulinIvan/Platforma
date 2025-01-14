from django.urls import path
from companies import views

app_name = 'companies'

urlpatterns = [
    path('', views.company, name='company'),
    path('create_company/', views.create_company, name='create_company'),
    path('show/<slug:company_id>/', views.CompanyDetail.as_view(), name='show_company'),
]