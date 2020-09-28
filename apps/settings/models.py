from django.db import models


# Create your models here.

class mainPageSettings(models.Model):
    title = models.CharField(max_length=255, help_text="设置网站名称", verbose_name="网站名称")
