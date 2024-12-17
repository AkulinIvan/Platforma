from rest_framework import viewsets
from .serializers import CallSerializer

from django.shortcuts import render
from .models import CallLog

def call_list(request):
    calls = CallLog.objects.all().order_by('-start_time')
    return render(request, 'ATS/call_list.html', {'calls': calls})


class CallViewSet(viewsets.ModelViewSet):
    queryset = CallLog.objects.all()
    serializer_class = CallSerializer
