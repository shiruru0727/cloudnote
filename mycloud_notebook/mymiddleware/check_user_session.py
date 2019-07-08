from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

from user.models import User


class mymiddleware(MiddlewareMixin):
    def process_request(self, request):
        if hasattr(request, 'session') and 'userinfo' in request.session:
            # 此时用户已登陆
            # 拿到用户id
            user_id = request.session['userinfo']['id']
            # 根据当前登陆用户找到当前用户
            user = User.objects.get(id=user_id)
        else:
            return render(request,"index.html")
            # raise Http404
