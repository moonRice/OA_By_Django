from django.shortcuts import render
from django.views import View

# Create your views here.
from apps.user.models import User


class showIndex(View):
    """返回个人事务中心页面"""

    def get(self, request):
        context = {
            'flag': 'idx',
        }
        return render(request, 'personal_page.html', context)

    def post(self, request):
        context = {
            'errmsg': '',
        }
        return render(request, 'ERROR_pages/err_page.html', context)


class showOAIndex(View):
    """返回OA页面"""

    def get(self, request):
        # username = request.COOKIES.get('username')
        user = request.user

        try:
            user = User.objects.get(username=user)
        except User.DoesNotExist:
            user.username = 'DoesNotExist'
        context = {
            'flag': 'kssy',
            'user': user
        }
        return render(request, 'oa_default_page.html', context)

    def post(self, request):
        context = {
            'errmsg': '',
        }
        return render(request, 'ERROR_pages/err_page.html', context)


class showAdminDocs(View):
    def get(self, request):
        return render(request, 'AdminDoc/idx.html')

    def post(self, request):
        pass
