import datetime

import json

from django.db.models import Count
from django.http import JsonResponse, HttpResponse

from django.shortcuts import render

from django.views import View
from ExtraFunction.CMDColor import Colored

from .models import LXMB, XMLX, XMSJ, XXSJ, TPXM, tongji, tongjiCount

# Create your views here.
from ..user.models import BankAccount, User

"""展示投票系统主页"""


class showIndex(View):
    def get(self, request):
        color = Colored()
        current_time = datetime.datetime.now()
        context = {
            'flag': 'tpxt',
        }
        # username = request.COOKIES.get('username')
        user = request.user
        print(color.blue('[' + str(current_time) + '] --> ' + user.username + '打开了投票系统首页'))

        return render(request, 'TouPiaoXiTong/idx.html', context)

    def post(self, request):
        pass


class showAllVoteProjects(View):
    def get(self, request):
        color = Colored()
        current_time = datetime.datetime.now()

        allV = TPXM.objects.all()

        context = {
            'flag2': 'cktpxm',
            'all': allV
        }
        # username = request.COOKIES.get('username')
        user = request.user
        print(color.blue('[' + str(current_time) + '] --> ' + user.username + '打开了所有投票票件列表'))
        return render(request, 'TouPiaoXiTong/cktpxm.html', context)

    def post(self, requwst):
        pass


class showAddVoteProjects(View):

    def get(self, request):
        color = Colored()
        current_time = datetime.datetime.now()
        context = {
            'flag2': 'cjxtp',
        }
        # username = request.COOKIES.get('username')
        user = request.user
        print(color.blue('[' + str(current_time) + '] --> ' + user.username + '打开了添加投票的页面'))
        return render(request, 'TouPiaoXiTong/cjxtp.html', context)

    def post(self, requwst):
        pass


class showModels(View):

    def get(self, request):
        color = Colored()
        current_time = datetime.datetime.now()
        user = request.user

        try:
            LXMB.objects.all()
        except LXMB.DoesNotExist:
            print(color.blue('[' + str(current_time) + '] --> ' + user.username + '打开了票件模板的页面，可惜里面并没有模板文件'))
            return render(request, 'TouPiaoXiTong/ckmbwj.html', {
                'msg': '暂无模板文件，请在后台创建'
            })
        all_models = LXMB.objects.all()
        lxmc_list = []
        for a in all_models:
            b = XMLX.objects.get(id=a.id)
            lxmc_list.append(b)

        context = {
            'flag2': 'ckmbwj',
            'mb': all_models,
            'lxmc_list': lxmc_list,
        }
        # username = request.COOKIES.get('username')

        print(color.blue('[' + str(current_time) + '] --> ' + user.username + '打开了票件模板的页面'))
        return render(request, 'TouPiaoXiTong/ckmbwj.html', context)

    def post(self, requwst):
        pass


def useModel(request, mb_id):
    color = Colored()
    current_time = datetime.datetime.now()
    username = request.user
    mb = LXMB.objects.get(MBID=mb_id)
    mbmc = XMLX.objects.get(LXID=str(mb))
    # mblx = XMLXZD
    user = User.objects.get(username=username)
    cjr = BankAccount.objects.get(account_id=user.id)

    context = {
        'mb': mb,
        'mbmc': mbmc,
        'cjr': cjr,
        'cjrq': current_time
    }
    print(mb)
    return render(request, 'TouPiaoXiTong/XMMB/' + str(mb.MBID) + '.html', context)


def startVote(request, pj_id):
    vote = TPXM.objects.get(XMID=pj_id)
    mb_id = LXMB.objects.get(LXID_id=vote.XMLX_id)
    wt = XMSJ.objects.get(tpxm=vote.id)
    xx = wt.XXID.all()
    # print(xx)
    context = {
        'vote': vote,
        'wt': wt,
        'xx': xx

    }
    return render(request, 'TouPiaoXiTong/TPYM/' + str(mb_id) + '.html', context)


def tongjiFunc(request):
    color = Colored()
    current_time = datetime.datetime.now()
    # gender = request.POST.get("gender")
    # AH = request.POST.getlist("aihao")
    username = request.user
    choice = request.POST.get('tp')
    if not choice:
        return render(request, 'TouPiaoXiTong/ok.html', {
            'msg': '您没选哦~我帮您跳回首页吧，不客气~~~:)',
            'sMSG': '哦不好意思，我不会做自动跳转。。。您自己点点吧~~'
        })
    else:
        print(color.yellow(
            '[' + str(current_time) + '] --> ' + str(username) + '选择了' + str(XXSJ.objects.get(XXID=choice))))
        try:
            tongjiCount.objects.get(XXID=(XXSJ.objects.get(XXID=choice)))
        except tongjiCount.DoesNotExist:
            data = tongjiCount(XXID=(XXSJ.objects.get(XXID=choice)), COUNT=0)
            data.save()
            data2 = tongjiCount.objects.get(XXID=(XXSJ.objects.get(XXID=choice)))
            temp = data2.COUNT
            data2.COUNT = temp + 1
            data2.save()
            tj = tongji(XXID=(XXSJ.objects.get(XXID=choice)),
                        TPR=(BankAccount.objects.get(account=(User.objects.get(username=username)))))
            tj.save()
            print(color.blue('[' + str(current_time) + '] --> ' + str(username) + '的选择在数据库中是新创建的，并且成功写入了数据库'))
            # print(choice)
            return render(request, 'TouPiaoXiTong/ok.html', {
                'msg': '投票成功'
            })
        data = tongjiCount.objects.get(XXID=(XXSJ.objects.get(XXID=choice)))
        temp = data.COUNT
        data.COUNT = temp + 1
        data.save()

        tj = tongji(XXID=(XXSJ.objects.get(XXID=choice)),
                    TPR=(BankAccount.objects.get(account=(User.objects.get(username=username)))))
        tj.save()
        print(color.blue('[' + str(current_time) + '] --> ' + str(username) + '的选择成功写入了数据库'))
        # print(choice)
        return render(request, 'TouPiaoXiTong/ok.html', {
            'msg': '投票成功'
        })


def tjsj(request):
    data = tongjiCount.objects.all()[:100]
    print(data)
    json_list = []
    for a in data:
        json_dict = {}
        json_dict["name"] = a.XXID
        json_dict["count"] = a.COUNT
        json_list.append(json_dict)
    context = {
        'data': data,
        'flag2': 'sjtj',
    }
    # return render(request, 'TouPiaoXiTong/zssj.html', context)
    return HttpResponse(json.dump(json_list), content_type="application/json")
