from django.urls import path
from ATS.views import call_list

app_name = 'ATS'

urlpatterns = [
    path('', call_list, name='call_list'),
]