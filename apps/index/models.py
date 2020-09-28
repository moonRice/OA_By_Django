from django.db import models

# Create your models here.
class siteSettings(models.Model):
    title = models.CharField(max_length=255, verbose_name='单位名称')