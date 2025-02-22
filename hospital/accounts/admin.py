from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from typing import Tuple, Any

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = User
    list_display: Tuple[str, ...] = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active', 'date_joined')
    list_filter: Tuple[str, ...] = ('role', 'is_staff', 'is_active')
    search_fields: Tuple[str, ...] = ('username', 'email', 'first_name', 'last_name')
    ordering: Tuple[str, ...] = ('-date_joined',)
    
    fieldsets: Tuple[Tuple[Any, dict], ...] = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('email', 'role', 'first_name', 'last_name')}),  
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets: Tuple[Tuple[Any, dict], ...] = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'first_name', 'last_name', 'is_active', 'is_staff')}
        ),
    )

admin.site.register(User, CustomUserAdmin)
