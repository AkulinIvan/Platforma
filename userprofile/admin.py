from django.contrib import admin

from .models import Userprofile

#admin.site.register(Userprofile) 


    
@admin.register(Userprofile)
class UserprofileAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ['user', 'role', 'phone', 'company', 'nomer_АТС']
    list_editable = ['role']
    search_fields = ['role', 'company']
    list_filter = ['role', 'company']
    fields = [
        'role',
        'phone',
        'company',
        'nomer_АТС',
    ]
    

