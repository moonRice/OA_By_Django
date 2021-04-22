from django.db import models
import django.utils.timezone as timezone
from froala_editor.fields import FroalaField

# Create your models here.
from apps.user.models import User, BankAccount, BankDepartment


class XXSJ(models.Model):
    XXID = models.IntegerField(verbose_name='选项ID')
    XXSJ = FroalaField(verbose_name='选项内容')

    def __str__(self):
        return '%s' % self.XXSJ

    class Meta:
        db_table = 'OA_VS_XXSJ'
        verbose_name = '选项数据'
        verbose_name_plural = verbose_name


class XMSJ(models.Model):
    SJID = models.IntegerField(verbose_name='数据ID')
    WT = FroalaField(verbose_name='问题内容')
    XXID = models.ManyToManyField(XXSJ, verbose_name='选项ID', help_text='对应的选项ID')

    def __str__(self):
        return '%s' % self.WT

    class Meta:
        db_table = 'OA_VS_XMSJ'
        verbose_name = '项目数据'
        verbose_name_plural = verbose_name


class XMLX(models.Model):
    LXID = models.IntegerField(verbose_name='票件类型ID')
    LXMC = models.CharField(max_length=255, verbose_name='类型名称')

    def __str__(self):
        return '%s' % self.LXMC

    class Meta:
        db_table = 'OA_VS_ZD_XMLX'
        verbose_name = '项目类型字典'
        verbose_name_plural = verbose_name


class TPXM(models.Model):
    XMID = models.IntegerField(verbose_name='票件项目ID')
    XMMC = models.CharField(max_length=255, verbose_name='票件项目名称')
    XMLX = models.OneToOneField(XMLX, on_delete=models.DO_NOTHING,
                                verbose_name='票件类型')
    CJRQ = models.DateTimeField('保存日期', default=timezone.now)
    CJR = models.OneToOneField(BankAccount, on_delete=models.DO_NOTHING,
                               verbose_name='创建人账号',
                               help_text='选择创建人')
    CYR = models.ManyToManyField(BankDepartment,
                                 verbose_name='参与人员',
                                 help_text='选择可以参与投票的人')
    SJID = models.ManyToManyField(XMSJ,
                                  verbose_name='投票内容',
                                  help_text='与问题数据进行对接')

    def __str__(self):
        return '%s' % self.XMMC

    class Meta:
        db_table = 'OA_VS_XM'
        verbose_name = '投票项目'
        verbose_name_plural = verbose_name


class XMZTZD(models.Model):
    ZTID = models.IntegerField(verbose_name='票件项目ID')
    ZTMC = models.CharField(max_length=255, verbose_name='状态名称')

    def __str__(self):
        return '%s' % self.ZTMC

    class Meta:
        db_table = 'OA_VS_ZD_XMZT'
        verbose_name = '项目状态字典'
        verbose_name_plural = verbose_name


class XMZT(models.Model):
    XMID = models.OneToOneField(TPXM, on_delete=models.DO_NOTHING,
                                verbose_name='票件项目ID')
    XMZT = models.OneToOneField(XMZTZD, on_delete=models.DO_NOTHING,
                                verbose_name='票件项目状态')

    def __str__(self):
        return '%s' % self.XMZT

    class Meta:
        db_table = 'OA_VS_XMZT'
        verbose_name = '项目状态'
        verbose_name_plural = verbose_name


class LXMB(models.Model):
    LXID = models.ForeignKey(XMLX, on_delete=models.DO_NOTHING,
                             verbose_name='投票类型ID')
    MBID = models.IntegerField(verbose_name='模板ID')
    MBNR = FroalaField(verbose_name='模板代码')
    BZXX = models.CharField(max_length=255, verbose_name='备注信息')

    def __str__(self):
        return '%s' % self.MBID

    class Meta:
        db_table = 'OA_VS_LXMB'
        verbose_name = '票件类型模板'
        verbose_name_plural = verbose_name


class tongji(models.Model):
    XXID = models.ForeignKey(XXSJ, on_delete=models.DO_NOTHING, verbose_name='选项ID')
    TPR = models.ForeignKey(BankAccount, on_delete=models.DO_NOTHING, verbose_name='投票人')
    TPSJ = models.DateTimeField('投票日期')

    def __str__(self):
        return '%s' % self.TPR

    class Meta:
        db_table = 'OA_VS_tj'
        verbose_name = '投票统计'
        verbose_name_plural = verbose_name


class tongjiCount(models.Model):
    XXID = models.ForeignKey(XXSJ, on_delete=models.DO_NOTHING, verbose_name='选项ID')
    COUNT = models.IntegerField(verbose_name='投票次数', default=0)

    def __str__(self):
        return '%s' % self.XXID

    class Meta:
        db_table = 'OA_VS_tj_count'
        verbose_name = '投票统计_数量统计'
        verbose_name_plural = verbose_name
