from django.conf import settings
from django.db import models
from apps.user.models import User
from db.base_model import BaseModel

from mdeditor.fields import MDTextField


# Create your models here.
class guestBook(BaseModel):
    title = models.CharField(max_length=255, verbose_name='标题')
    auth = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='发言人')
    text = MDTextField(verbose_name='留言内容')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'chats_guestbook'
        verbose_name = '留言簿'
        verbose_name_plural = verbose_name


class reply(BaseModel):
    auth = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='回复人')
    text = MDTextField(verbose_name='回复内容')
    forWhichGuestbook = models.ForeignKey(guestBook, on_delete=models.DO_NOTHING, verbose_name='所属的留言')

    # def __str__(self):
    #     return self.forWhichGuestbook

    class Meta:
        db_table = 'chats_reply'
        verbose_name = '回复'
        verbose_name_plural = verbose_name
