from django.contrib import admin
import options.settings as a

# Register your models here.
# 修改网页title和站点header。
admin.site.site_title = a.ADMIN_SITE_TITLE_2
admin.site.site_header = a.ADMIN_SITE_TITLE_1
