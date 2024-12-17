from rest_framework import serializers
from .models import CallLog

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallLog
        fields = ['callee', 'caller', 'recording']