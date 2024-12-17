from django.contrib import admin

from .models import CallLog, PhoneNumber

admin.site.register(CallLog) 
admin.site.register(PhoneNumber)
    
# @admin.register(CallLog)
# class CallLogAdmin(admin.ModelAdmin):
#     exclude = ('caller',)
#     list_display = ['caller', 'callee', 'start_time', 'end_time']
#     list_filter = ['caller', 'callee', 'start_time', 'end_time']
#     fields = [
#         'caller',
#         'callee',
#         'start_time',
#         'end_time',
#     ]
    