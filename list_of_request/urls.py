from django.urls import path, re_path, register_converter
from list_of_request import views
from rest_framework import routers
from . import converters

app_name = 'list_of_request'

register_converter(converters.FourDigitYearConverter, 'year4')

# router = routers.DefaultRouter()
# router.register(r'applications', views.ArticlesViewSet, basename='applications')
# print(router.urls)

urlpatterns = [
    path('', views.list_applications, name='applications'),
    path('new-application/', views.new_applications_list, name='new_applications'),
    path('<int:pk>/', views.ApplicationDetail.as_view(), name='application'),
    path('create/', views.create_application, name='create_application'),
    path('search/', views.ApplicationSearchList.as_view(), name='search_application'),
    path('<int:pk>/delete/', views.application_delete, name='delete_application'),
    path('<int:pk>/edit/', views.application_edit, name='edit_application'),
    path('<int:pk>/convert/', views.convert_to_complete_application, name='convert_application'),
    path('complete-applications/', views.complete_applications, name='complete_applications'),
    path('complete-applications/<int:pk>/', views.ApplicationCompleteDetail.as_view(), name='detail_complete_application'),
    path('assigned-applications/', views.assigned_applications, name='assigned_applications'),
    path('assigned-applications/<int:pk>/', views.ApplicationAssignDetail.as_view(), name='detail_assigned_applications'),
    # path('export-applications/', views.table_view, name='export_url'),
    # path('archive/<year4:year>/', views.archive, name='archive'),
    # path('api/v1/applications/', views.ArticlesAPIList.as_view()),
    # path('api/v1/applications/<int:pk>/', views.ArticlesAPIUpdate.as_view()),
    # path('api/v1/applicationsdelete/<int:pk>/', views.ArticlesAPIDestroy.as_view()),
    #path('api/v1/', include(router.urls))
    
    
]