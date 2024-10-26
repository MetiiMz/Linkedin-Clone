from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('full_name', 'email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'phone_number', 'password')}),
        ('Permission', {'fields': ('is_active', 'is_admin', 'last_login')})
    )
    add_fieldsets = (
        (None, {'fields': ('full_name', 'email', 'phone_number', 'password1', 'password2')}),
    )
    search_fields = ('full_name', 'email')
    ordering = ('full_name',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
