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
# 登陆装饰器
from . import views
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import showIndex, showAllVoteProjects, showAddVoteProjects, showModels

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('VoteSystemIndex/', login_required(showIndex.as_view()), name='index'),
    path('ShowAllVoteProjects/', login_required(showAllVoteProjects.as_view()), name='cktpxm'),
    path('ShowAddVoteProjects/', login_required(showAddVoteProjects.as_view()), name='cjxtp'),
    path('ShowModels/', login_required(showModels.as_view()), name='ckmbwj'),
    path('USerModels/<int:mb_id>', login_required(views.useModel), name='symb'),
    path('StartVote/<int:pj_id>', login_required(views.startVote), name='kstp'),
    path('TongJi/', login_required(views.tongjiFunc), name='tptj'),
    path('Data/', login_required(views.tjsj), name='tjsj'),
]
