from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User, Profile, MenuSections


class ProfileInlined(admin.StackedInline):
    model = Profile
    can_delete = False
    

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInlined, )
    # readonly_fields=('user_friends',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    autocomplete_fields = ["sections", ]
    fieldsets = (
        (
            None,
            {
                'fields': ('username', 'password')
            }
        ),
        (
            'Персональные данные',
            {
                'fields': ('first_name',
                           'patronymic',
                           'last_name',
                           'email',
                           'cookie_acceptance',
                           'sections',
                           'job')
            }
        ),        
        (
            'Разрешения',
            {
                'fields': ('is_active',
                           'is_staff',
                           'is_admin',
                           'is_dispatcher',
                           'is_executor',
                           'is_master',
                           'is_duty_executor',
                           'is_duty_dispatcher',
                           'groups',
                           'user_permissions'),
            }
        )
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_first_name', 'user_last_name', 'user_email', 'gender', 'birthday_at')
    list_editable = ('gender', 'birthday_at')

    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.short_description = 'Имя'

    def user_last_name(self, obj):
        return obj.user.last_name
    user_last_name.short_description = 'Фамилия'

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = "Email"


@admin.register(MenuSections)
class MenuSectionsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ["name"]
