
from django.contrib import admin

from .models import  Master, Company, City, Roles, Status_application, Street, House, Type_application, View_application, Usernames, Worker

admin.site.register(Company)
admin.site.register(City)
admin.site.register(Street)
admin.site.register(House)
admin.site.register(Type_application)
admin.site.register(View_application)
admin.site.register(Status_application)
admin.site.register(Master)
admin.site.register(Worker)
admin.site.register(Usernames)
admin.site.register(Roles)
