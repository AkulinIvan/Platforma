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
    exclude = ('created_by',)
    # prepopulated_fields = {'street': ('house',)}
    list_display = ['fio', 'phone', 'text', 'create_time', 'last_update', 'street', 'house', 'flat', 'worker', 'user']
    list_editable = ['worker']
    search_fields = ['street', 'worker', 'fio']
    list_filter = ['street', 'worker', 'create_time', 'phone']
    fields = [
        'create_time',
        'last_update',
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


