from import_export.admin import ImportExportModelAdmin as exp
from django.contrib import admin
from .models import TPXM, XMZT, XMZTZD, XMLX, LXMB, XXSJ, XMSJ, tongji, tongjiCount


# Register your models here.
# 富文本编辑器
# admin.site.register(ti)

@admin.register(tongjiCount)
class tongjicountManage(exp):
    list_display = (
        'XXID',
        'COUNT'
    )


@admin.register(tongji)
class tongjiManage(exp):
    list_display = (
        'XXID',
        'TPR',
        'TPSJ'
    )


@admin.register(TPXM)
class tpxmManage(exp):
    list_display = (
        'XMID',
        'XMMC',
        'XMLX',
        'CJRQ',
        'CJR'
    )


@admin.register(XMZT)
class xmztManage(exp):
    list_display = (
        'XMID',
        'XMZT'
    )


@admin.register(XMZTZD)
class xmztzdManage(exp):
    list_display = (
        'ZTID',
        'ZTMC'
    )


@admin.register(XMLX)
class xmlxManage(exp):
    list_display = (
        'LXID',
        'LXMC'
    )


@admin.register(LXMB)
class lxmbManage(exp):
    list_display = (
        'LXID',
        'MBID',
        'MBNR',
        'BZXX'
    )


@admin.register(XMSJ)
class xmsjManage(exp):
    list_display = (
        'SJID',
        'WT',
    )


@admin.register(XXSJ)
class xxsjManage(exp):
    list_display = (
        'XXID',
        'XXSJ'
    )
