import re

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from apps.user.models import User


# Create your views here.
class registerPage(View):
    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        # 接收数据
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        # 进行数据校验
        if not username:
            return render(request, 'user/register.html', {'errmsg': '用户名没有写', 'back_email': email})
        else:
            if not password1:
                return render(request, 'user/register.html',
                              {'errmsg': '密码没有写', 'back_username': username, 'back_email': email})
            else:
                if not password2:
                    return render(request, 'user/register.html',
                                  {'errmsg': '二次密码没有写', 'back_username': username, 'back_email': email})
                elif password1 != password2:
                    return render(request, 'user/register.html',
                                  {'errmsg': '两次密码不一样', 'back_username': username, 'back_email': email})
                else:
                    if not email:
                        return render(request, 'user/register.html',
                                      {'errmsg': '邮箱没有写', 'back_username': username, 'back_password1': password1,
                                       'back_password2': password2})
                    # 正则表达式校验邮箱地址合法性
                    elif not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
                        return render(request, 'user/register.html',
                                      {'errmsg': '邮箱格式不正确', 'back_username': username,
                                       'back_password1': password1, 'back_password2': password2})

        # if allow != 'on':
        #     return render(request, 'user/register.html', {'errmsg': '请同意协议'})

        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            # 用户名已存在
            return render(request, 'user/register.html', {'errmsg': '用户名已存在'})

        user = User.objects.create_user(username, email, password1)
        user.is_active = 0
        user.save()

        # 返回应答，跳转到首页

        return render(request, 'user/login.html')
        # redirect(reverse('user:register'))


"""登录业务代码"""


class loginPage(View):
    def get(self, request):
        """显示登录页面"""
        # 判断是否记住了用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''

        # 使用模板
        return render(request, 'user/login.html', {'username': username, 'checked': checked})

    def post(self, request):
        """登录校验"""
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 校验数据
        if not all([username, password]):
            return render(request, 'user/login.html', {'errmsg': '数据不完整'})

        # 业务处理:登录校验
        user = authenticate(username=username, password=password)
        if user is not None:
            # 用户名密码正确
            if user.is_active:
                # 用户已激活
                # 记录用户的登陆状态
                # 天坑！！！！！！！
                # 未激活用户依旧返回None
                # 详见settings解决方案
                login(request, user)

                # 登陆装饰器
                # 获取登陆后所要跳转的地址
                next_url = request.GET.get('next', reverse('oa_index:oa_index'))

                # 假若这个人故意删除next后面的地址，则next_URL = None
                # 后面的response就会报错
                # 所以在最后要设置默认跳转，以防小人捣乱

                # 跳转到接收到的next值
                response = redirect(next_url)  # HttpResponseRedirect

                # 判断是否需要记住用户名
                remember = request.POST.get('remember')

                if remember == 'on':
                    # 记住用户名
                    response.set_cookie('username', username, max_age=7 * 24 * 3600)
                else:
                    response.delete_cookie('username')

                # 返回response
                return response
            else:
                # 用户未激活
                return render(request, 'user/login.html', {'errmsg': '账户未激活'})
        else:
            # 用户名或密码错误
            return render(request, 'user/login.html', {'errmsg': '用户名或密码错误'})


# /user/logout
class LogoutView(View):
    """退出登录"""

    def get(self, request):
        """退出登录"""
        # 清除用户的session信息
        logout(request)

        # 跳转到首页
        return redirect(reverse('oa_index:oa_index'))
