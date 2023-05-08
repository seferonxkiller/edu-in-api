from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from .forms import AccountCreationForm, AccountChangeForm


@admin.action(description="Set to student")
def set_to_student(modeladmin, request, queryset):
    queryset.update(role=0, is_staff=False)


@admin.action(description="Set to teacher")
def set_to_teacher(modeladmin, request, queryset):
    queryset.update(role=1, is_staff=False)


@admin.action(description="Set to staff")
def set_to_teacher(modeladmin, request, queryset):
    queryset.update(role=2, is_staff=True)


class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'role', 'password1', 'password2'), }),
    )
    actions = [set_to_student, set_to_teacher]
    list_display = ('id', 'email', 'first_name', 'last_name', 'image_tag', 'get_role_display', 'is_superuser', 'is_staff','is_active', 'date_modified', 'date_created')
    ordering = None
    readonly_fields = ('date_modified', 'date_created')
    list_filter = ('date_created', 'role', 'is_superuser', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'image')}),
        ('Permissions', {'fields': ('role', 'is_superuser', 'is_staff', 'is_active',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('date_modified', 'date_created')}),
    )
    search_fields = ('first_name', 'email', 'last_name')




admin.site.register(Account, AccountAdmin)
