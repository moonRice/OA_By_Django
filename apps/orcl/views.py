from django.shortcuts import render
from django.views import View

from .models import orcl_ljcs, orcl_cz, orcl_cz_ls

import cx_Oracle

from ExtraFunction.CMDColor import Colored
import datetime

# Create your views here.
from ..user.models import BankAccount, User


class showIndex(View):
    def get(self, request):
        color = Colored()
        current_time = datetime.datetime.now()
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
        else:
            ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
        # print(ip)

        print(color.blue('[' + str(current_time) + '] --> ' + ip + '打开了数据库操作页面'))

        info = orcl_cz.objects.all()
        context = {
            'info': info
        }
        return render(request, 'orcl/idx.html', context)

    def post(self, request):
        pass


def jlip(request, czID):
    cz = orcl_cz.objects.get(id=czID)
    color = Colored()
    current_time = datetime.datetime.now()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    # print(ip)

    print(color.blue('[' + str(current_time) + '] --> ' + ip + '执行了' + cz.czmc + '操作'))

    username = request.user
    ls = orcl_cz_ls(ip=str(ip), isSuccess='是', czbm=(orcl_cz.objects.get(id=czID)),
                    czr=(BankAccount.objects.get(account=(User.objects.get(username=username)))))
    ls.save()


def runSQL(request, cz_id):
    cz = orcl_cz.objects.get(id=cz_id)
    if cz.czbm == 'select':
        orcl = orcl_ljcs.objects.get(id=cz.orcl_id)
        db = cx_Oracle.connect(orcl.username, orcl.password, orcl.ip + ':' + orcl.port + '/' + orcl.serverName)
        cur = db.cursor()
        print('select ' + str(cz.zd) + ' from ' + str(cz.bmc))
        # cur.execute(str(cz.sql))
        cur.execute('select ' + str(cz.zd) + ' from ' + str(cz.bmc))
        zd = db.cursor()
        # zd.execute("select A.COLUMN_NAME,A.DATA_TYPE  from user_tab_columns A where TABLE_NAME='" + str(cz.bmc) + "'")
        zd.execute("select A.COLUMN_NAME from user_tab_columns A where TABLE_NAME='" + str(cz.bmc) + "'")
        r = zd.fetchall()
        print(r)
        rows = cur.fetchall()
        for row in rows[:10]:
            print(f"{row[0]} ,", end='')
        db.close()

        jlip(request, cz_id)

        context = {
            'db': rows,
            'zd': r
        }
        return render(request, 'orcl/cz/select.html', context)

    elif cz.czbm == 'update':
        orcl = orcl_ljcs.objects.get(id=cz.orcl_id)
        db = cx_Oracle.connect(orcl.username, orcl.password, orcl.ip + ':' + orcl.port + '/' + orcl.serverName)
        cur = db.cursor()
        cur.execute(str(cz.sql))
        print(cur)
        db.close()
        jlip(request, cz_id)
        return render(request, 'orcl/cz/update.html', {
            'msg': '执行成功'
        })
