from django.http import HttpResponse
from django.views import View


class UserView(View):
    def get(self, request):
        # esay = request.GET.get('essay')
        print('dssdssdsdsdds')
        return HttpResponse('dsds')