from django.shortcuts import render
from django.views import View


# Create your views here.

class showIndex(View):
    """返回个人事务中心页面"""

    def get(self, request):
        context = {
            'flag': 'idx',
        }
        return render(request, 'main_page.html', context)

    def post(self, request):
        context = {
            'errmsg': '',
        }
        return render(request, 'ERROR_pages/err_page.html', context)


class showOAIndex(View):
    """返回个人事务中心页面"""

    def get(self, request):
        context = {
            'flag': 'idx',
        }
        return render(request, 'oa_default_page.html', context)

    def post(self, request):
        context = {
            'errmsg': '',
        }
        return render(request, 'ERROR_pages/err_page.html', context)
