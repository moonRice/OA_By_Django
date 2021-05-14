import django.utils.timezone as timezone

from django.db import models

# Create your models here.
from apps.user.models import BankAccount


class orcl_ljcs(models.Model):
    ip = models.CharField(max_length=255, verbose_name='IP地址')
    port = models.CharField(max_length=255, verbose_name='端口号')
    serverName = models.CharField(max_length=255, verbose_name='数据库名称')
    username = models.CharField(max_length=255, verbose_name='数据库登陆账号')
    password = models.CharField(max_length=255, verbose_name='数据库登陆密码')
    mc = models.CharField(max_length=255, verbose_name='服务器名称')

    def __str__(self):
        return '%s' % self.mc

    class Meta:
        db_table = 'orcl_ljcs'
        verbose_name = '数据库连接参数'
        verbose_name_plural = verbose_name


class orcl_cz(models.Model):
    orcl = models.ForeignKey(orcl_ljcs, on_delete=models.DO_NOTHING, verbose_name='连接的库')
    czbm = models.CharField(max_length=255, verbose_name='操作编码')
    czmc = models.CharField(max_length=255, verbose_name='操作名称')
    sysm = models.CharField(max_length=255, verbose_name='使用说明')
    isDanger = models.CharField(max_length=255, verbose_name='操作是否危险')
    sql = models.CharField(max_length=255, verbose_name='SQL语句')
    bmc = models.CharField(max_length=255, verbose_name='要查询的表名称')
    zd = models.CharField(max_length=255, verbose_name='要查询的字段')
    imgURL = models.CharField(max_length=255, verbose_name='图片地址')

    def __str__(self):
        return '%s' % self.czmc

    class Meta:
        db_table = 'orcl_cz'
        verbose_name = '操作信息'
        verbose_name_plural = verbose_name


class orcl_cz_ls(models.Model):
    czbm = models.ForeignKey(orcl_cz, on_delete=models.DO_NOTHING, verbose_name='操作名称')
    czr = models.ForeignKey(BankAccount, on_delete=models.DO_NOTHING, verbose_name='操作人')
    ip = models.CharField(max_length=255, verbose_name='操作人IP地址')
    czsj = models.DateTimeField('操作时间', default=timezone.now)
    isSuccess = models.CharField(max_length=255, verbose_name='是否成功操作')

    def __str__(self):
        return '%s' % self.czr

    class Meta:
        db_table = 'orcl_cz_ls'
        verbose_name = '操作历史'
        verbose_name_plural = verbose_name
