from django.contrib import admin
from import_export.admin import ImportExportModelAdmin as exp

from .models import orcl_cz, orcl_ljcs, orcl_cz_ls


# Register your models here.
@admin.register(orcl_cz)
class czManage(exp):
    list_display = (
        'orcl',
        'czbm',
        'czmc',
        'isDanger',
        'bmc',
        'zd',
    )


@admin.register(orcl_ljcs)
class ljcsManage(exp):
    list_display = (
        'ip',
        'port',
        'serverName',
        'username',
        'mc'
    )


@admin.register(orcl_cz_ls)
class czlsManage(exp):
    list_display = (
        'czbm',
        'czr',
        'ip',
        'czsj',
        'isSuccess'
    )
