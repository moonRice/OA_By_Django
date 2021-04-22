from django.contrib import admin
from .models import TPXM, XMZT, XMZTZD, XMLX, LXMB, XXSJ, XMSJ, tongji, tongjiCount


# Register your models here.
# 富文本编辑器
# admin.site.register(ti)

@admin.register(tongjiCount)
class tongjicountManage(admin.ModelAdmin):
    list_display = (
        'XXID',
        'COUNT'
    )


@admin.register(tongji)
class tongjiManage(admin.ModelAdmin):
    list_display = (
        'XXID',
        'TPR',
        'TPSJ'
    )


@admin.register(TPXM)
class tpxmManage(admin.ModelAdmin):
    list_display = (
        'XMID',
        'XMMC',
        'XMLX',
        'CJRQ',
        'CJR'
    )


@admin.register(XMZT)
class xmztManage(admin.ModelAdmin):
    list_display = (
        'XMID',
        'XMZT'
    )


@admin.register(XMZTZD)
class xmztzdManage(admin.ModelAdmin):
    list_display = (
        'ZTID',
        'ZTMC'
    )


@admin.register(XMLX)
class xmlxManage(admin.ModelAdmin):
    list_display = (
        'LXID',
        'LXMC'
    )


@admin.register(LXMB)
class lxmbManage(admin.ModelAdmin):
    list_display = (
        'LXID',
        'MBID',
        'MBNR',
        'BZXX'
    )


@admin.register(XMSJ)
class xmsjManage(admin.ModelAdmin):
    list_display = (
        'SJID',
        'WT',
    )


@admin.register(XXSJ)
class xxsjManage(admin.ModelAdmin):
    list_display = (
        'XXID',
        'XXSJ'
    )
