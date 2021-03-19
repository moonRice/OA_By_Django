"""OA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from .views import loginPage, registerPage
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 展示注册登陆页面
    path('login', loginPage.as_view(), name='login'),
    path('register', registerPage.as_view(), name='register'),
    # 注册处理
    # path('register_handle', registerPage.as_view(), name='register_handle'),
]
