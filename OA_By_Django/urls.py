"""OA_By_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 总后台管理系统
    path('admin/', admin.site.urls),

    # 重做后台管理系统

    # 网站主页
    path('', include(('apps.index.urls', 'index'), namespace='index')),

    # OA主页
    path('oa/', include(('apps.index.urls', 'oa_index'), namespace='oa_index')),

    # 无纸化办公
    path('wz/', include(('apps.WuZhiHuaBanGong.urls', 'oa_wzhbg'), namespace='oa_wzhbg')),

    # 用户
    path('user/', include(('apps.user.urls', 'user'), namespace='user')),


    # 留言簿
    path('guestbook/', include(('apps.chats.urls', 'guestbook'), namespace='guestbook')),


]
