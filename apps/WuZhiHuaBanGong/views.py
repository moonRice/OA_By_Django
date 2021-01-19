from django.shortcuts import render
from django.views import View


# Create your views here.


class showIndex(View):
    """返回无纸化办公首页"""

    def get(self, request):
        context = {
            'flag1': 'wzhbg',
            'flag2': 'sysm',
        }
        return render(request, 'WuZhiHuaBanGong/idx.html', context)

    def post(self, request):
        context = {
            'errmsg': '',
        }
        return render(request, 'ERROR_pages/err_page.html', context)

class showBaoxiuIndex(View):
    """返回设备报修首页"""

    def get(self, request):
        context = {
            'flag1': 'wzhbg',
            'flag2': 'sbbx',
        }
        return render(request, 'WuZhiHuaBanGong/SheBeiBaoXiu.html', context)

    def post(self, request):
        context = {
            'errmsg': '',
        }
        return render(request, 'ERROR_pages/err_page.html', context)