# Generated by Django 3.1.7 on 2021-04-20 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0002_auto_20201229_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='部门名称')),
            ],
            options={
                'verbose_name': '银行部门信息',
                'verbose_name_plural': '银行部门信息',
                'db_table': 'OA_BankDepartment_information',
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='姓名')),
                ('gender', models.SmallIntegerField(choices=[(0, '先生'), (1, '女士')], default=0, verbose_name='性别')),
                ('account',
                 models.OneToOneField(help_text='一一对应职工注册的账号，需要审核。', on_delete=django.db.models.deletion.DO_NOTHING,
                                      to=settings.AUTH_USER_MODEL, verbose_name='银行账号信息')),
                ('department',
                 models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='user.bankdepartment',
                                      verbose_name='所属银行部门')),
            ],
            options={
                'verbose_name': '银行用户个人信息',
                'verbose_name_plural': '银行用户个人信息',
                'db_table': 'OA_BankAccount_information',
            },
        ),
    ]
