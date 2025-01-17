from django.contrib import admin

from .models import Userprofile

#admin.site.register(Userprofile) 


    
@admin.register(Userprofile)
class UserprofileAdmin(admin.ModelAdmin):
    # exclude = ('user',)
    list_display = ['user', 'role', 'phone', 'nomer_ATS', 'is_admin', 'is_coordinator', 'is_executor', 'is_dispatcher', 'is_master', 
                    'is_duty_executor', 'is_duty_dispatcher']
    list_editable = ['role', 'is_admin', 'is_coordinator', 'is_executor', 'is_dispatcher', 'is_master', 
                    'is_duty_executor', 'is_duty_dispatcher']
    search_fields = ['role']
    list_filter = ['role']
    fields = [
        'user',
        'role',
        'phone',
        'nomer_ATS',
        'is_admin', 
        'is_coordinator', 
        'is_executor', 
        'is_dispatcher', 
        'is_master', 
        'is_duty_executor', 
        'is_duty_dispatcher'
    ]
    

