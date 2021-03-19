import re

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from apps.user.models import User


# Create your views here.
class loginPage(View):
    def get(self, request):
        context = {

        }
        return render(request, 'user/login.html', context)

    def post(self, request):
        pass


class registerPage(View):
    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        # 接收数据
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        # 数据校验
        if not all([username, password1, password2, email]):
            # 数据不完整
            context = {
                'username_error': '数据不完整',
                'password1_error': '数据不完整',
                'password2_error': '数据不完整',
                'email_error': '数据不完整',
            }
        if not re.match('[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'user/register.html', {
                'email_errmsg': '邮箱格式不对',
                'color_email': True
            })
        # 数据处理
        # user = User()
        # user.username = username
        # user.password = password1
        # user.email = email
        # user.save()
        user = User.objects.create_user(username, email, password1)

        # 返回应答，跳转到首页

        return render(request, 'user/register.html')
        # redirect(reverse('user:register'))

