from django.shortcuts import render
from django.views import View


# Create your views here.
class loginPage(View):
    def get(self, request):
        context = {

        }
        return render(request, 'login.html', context)

    def post(self, request):
        pass
