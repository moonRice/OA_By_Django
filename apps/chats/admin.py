from import_export.admin import ImportExportModelAdmin as exp
from django.contrib import admin
from .models import guestBook, reply


# Register your models here.
@admin.register(guestBook)
class guM(exp):
    list_display = (
        'title',
        'auth',
        'create_time',
        'text',
    )


@admin.register(reply)
class reM(exp):
    list_display = (
        'auth',
        'create_time',
        'text',
        'forWhichGuestbook',
    )
