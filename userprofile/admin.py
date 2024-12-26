from django.contrib import admin

from .models import Userprofile

#admin.site.register(Userprofile) 


    
@admin.register(Userprofile)
class UserprofileAdmin(admin.ModelAdmin):
    # exclude = ('user',)
    list_display = ['user', 'role', 'phone', 'nomer_ATS']
    list_editable = ['role']
    search_fields = ['role']
    list_filter = ['role']
    fields = [
        'user',
        'role',
        'phone',
        'nomer_ATS',
    ]
    

