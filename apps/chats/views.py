from django.shortcuts import render
from django.views import View
from .models import guestBook, reply
from ..user.models import User
import markdown


# Create your views here.


class showPage(View):
    def get(self, request):
        gb = guestBook.objects.all()
        context = {
            'flag': 'guestBook',
            'gb': gb,
        }
        return render(request, 'blogs/chat.html', context)

    def post(self, request):
        context = {
            'errmsg': '',
        }
        return render(request, 'ERROR_pages/err_page.html', context)


def gb_details(request, gb_id):
    gb = guestBook.objects.get(id=int(gb_id))
    gb.text = markdown.markdown(gb.text, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

    re = reply.objects.filter(forWhichGuestbook_id=gb_id)
    re_list = []
    for a in re:
        a.text = markdown.markdown(a.text, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        re_list.append(a)
    context = {
        'flag': 'guestBook',
        'gb_d': gb,
        're': re_list,
    }
    return render(request, 'blogs/chat_details.html', context)
