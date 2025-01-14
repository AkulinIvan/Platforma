from django.contrib import admin

from .models import Companies, Cities, Master, Worker, Type_application

admin.site.register(Companies)
admin.site.register(Cities)
admin.site.register(Master)
admin.site.register(Worker)
admin.site.register(Type_application)
