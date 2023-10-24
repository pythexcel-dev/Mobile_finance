from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('image_tag', 'email', 'first_name', 'last_name', 'role', 'mobile_number', 'adhar_number', 'imei_number', 'address', 'created_at', 'updated_at',)
    list_filter = ('is_staff', 'role')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'role', 'mobile_number', 'image', 'adhar_number', 'imei_number', 'address',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'role', 'mobile_number', 'adhar_number', 'imei_number','address', 'image', 'password1', 'password2'),
        }),
    )

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.image.url))
    
admin.site.register(CustomUser, CustomUserAdmin)

