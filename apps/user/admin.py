from django.contrib import admin
from .models import User, Group, Department, Account


# Register your models here.

@admin.register(User)
class UserManage(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'is_active',
    )


@admin.register(Group)
class UserManage(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Department)
class UserManage(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Account)
class UserManage(admin.ModelAdmin):
    list_display = (
        'username',
        'account',
        'gender',
    )
