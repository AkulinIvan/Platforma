from django.urls import path
from handbook import views


app_name = 'handbook'

urlpatterns = [
    path('', views.handbook, name='handbook'),
    path('company/', views.company, name='company'),
    path('create_company/', views.create_company, name='create_company'),
    path('city/', views.city, name='city'),
    path('street/', views.street, name='street'),
    path('create_street/', views.create_street, name='create_street'),
    path('house/', views.house, name='house'),
    path('create_house/', views.create_house, name='create_house'),
    path('type_application/', views.type_application, name='type_application'),
    path('view_application/', views.view_application, name='view_application'),
    path('status_application/', views.status_application, name='status_application'),
    path('executors/', views.executor, name='executor'),
    path('username/', views.username, name='username'),
]