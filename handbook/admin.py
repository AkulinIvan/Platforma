
from django.contrib import admin

from .models import  Roles, Status_application, Street, House, View_application



admin.site.register(Street)
admin.site.register(House)
admin.site.register(View_application)
admin.site.register(Status_application)

# admin.site.register(Usernames)
admin.site.register(Roles)
