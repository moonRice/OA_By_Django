from django.contrib import admin
from .models import guestBook, reply


# Register your models here.
@admin.register(guestBook)
class guM(admin.ModelAdmin):
    list_display = (
        'title',
        'auth',
        'create_time',
        'text',
    )


@admin.register(reply)
class reM(admin.ModelAdmin):
    list_display = (
        'auth',
        'create_time',
        'text',
        'forWhichGuestbook',
    )
