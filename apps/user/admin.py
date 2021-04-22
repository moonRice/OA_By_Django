from django.contrib import admin
from .models import User, Group, Department, Account, BankAccount, BankDepartment


# Register your models here.
@admin.register(BankAccount)
class BankAccountManage(admin.ModelAdmin):
    list_display = (
        'name',
        'account',
        'gender',
        'department'
    )


@admin.register(BankDepartment)
class BankDepartmentManage(admin.ModelAdmin):
    list_display = (
        'name',
    )


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
