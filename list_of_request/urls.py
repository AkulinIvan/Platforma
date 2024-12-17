from django.urls import path, include
from list_of_request import views
from rest_framework import routers

app_name = 'list_of_request'

# router = routers.DefaultRouter()
# router.register(r'applications', views.ArticlesViewSet, basename='applications')
# print(router.urls)

urlpatterns = [
    path('', views.ApplicationList.as_view(), name='applications'),
    path('application/<int:application_id>/', views.ApplicationDetail.as_view(), name='application'),
    path('create/', views.create_application, name='create_application'),
    path('search/', views.ApplicationSearchList.as_view(), name='search_application'),
    path('api/v1/applications/', views.ArticlesAPIList.as_view()),
    path('api/v1/applications/<int:pk>/', views.ArticlesAPIUpdate.as_view()),
    path('api/v1/applicationsdelete/<int:pk>/', views.ArticlesAPIDestroy.as_view()),
    #path('api/v1/', include(router.urls))
    
    
]