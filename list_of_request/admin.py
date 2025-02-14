from django.contrib import admin
from .models import  Articles


#admin.site.register(Articles)

class UserApplicationAdmin(admin.TabularInline):
    model = Articles
    fields = ['text', 'street', 'house', 'flat', 'fio', 'phone']
    search_fields = ['street', 'worker', 'fio']
    readonly_fields = ('street', 'house', 'flat', 'fio', 'user',)
    extra = 1
    
    
@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    # exclude = ('user',)
    # prepopulated_fields = {'street': ('house',)}
    list_display = ['priority', 'fio', 'phone', 'text', 'create_time', 'last_update', 'street', 'house', 'flat', 'worker', 'status']
    list_editable = ['worker']
    search_fields = ['street', 'worker', 'fio']
    list_filter = ['street', 'worker', 'create_time', 'phone', 'priority', 'status']
    readonly_fields = ['create_time', 'last_update']
    fields = [
        'create_time',
        'last_update',
        'status',
        'priority',
        ('street', 'house', 'flat'),
        ('fio', 'phone'),
        'text',
        'worker',
        'materials',
        'comment',
        
    ]
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)


