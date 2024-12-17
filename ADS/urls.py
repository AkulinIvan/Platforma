"""
URL configuration for ADS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from ATS.views import CallViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'calls', CallViewSet)
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('list_of_request/', include('list_of_request.urls', namespace='list_of_request')),
    path('user/', include('userprofile.urls', namespace='users')),
    path('handbook/', include('handbook.urls', namespace='handbook')),
    path('calls/', include('ATS.urls', namespace='ATS')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('sms/', include('sms_app.urls', namespace='sms')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls




