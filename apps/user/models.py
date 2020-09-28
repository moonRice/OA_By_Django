from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    """用户模型类"""

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fh_account_information'
        verbose_name = '账号信息'
        verbose_name_plural = verbose_name


class Group(models.Model):
    """职位信息模型类"""
    name = models.CharField(max_length=255, verbose_name='岗位名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fh_group_information'
        verbose_name = '职位信息'
        verbose_name_plural = verbose_name


class Department(models.Model):
    """部门信息模型类"""
    name = models.CharField(max_length=255, verbose_name='部门名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fh_Department_information'
        verbose_name = '部门信息'
        verbose_name_plural = verbose_name


class Account(models.Model):
    """账号信息模型类"""
    gender_choices = (
        (0, '先生'),
        (1, '女士'),
    )

    username = models.CharField(max_length=255, verbose_name='姓名')
    account = models.OneToOneField(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='账号信息',
        help_text='一一对应职工注册的账号，需要审核。'
    )
    gender = models.SmallIntegerField(default=0, choices=gender_choices, verbose_name='性别')
    group = models.OneToOneField(Group, on_delete=models.DO_NOTHING, verbose_name='职位信息')
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, verbose_name='所属部门')

    def __str__(self):
        return self.account

    class Meta:
        db_table = 'fh_staff_information'
        verbose_name = '教职工信息'
        verbose_name_plural = verbose_name
