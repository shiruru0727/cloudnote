from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.
from user import models


def mylogin(request):
    ''' 登录 '''
    if request.method == 'GET':
        return render(request, "user/login.html")
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = models.User.objects.get(name=username, password=password)
            # 将当前登录用户信息放入session
            request.session['userinfo'] = {
                "username": user.name,
                "id": user.id
            }
            # 登录成功跳回主页
            return HttpResponseRedirect("/")
        except:
            return HttpResponse("登录失败")


def myreg(request):
    ''' 注册 '''
    if request.method == 'GET':
        return render(request, "user/register.html")
    elif request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # 表单验证
        if username == '':
            username_error = "用户名不能为空"
            return render(request, 'user/register.html', locals())
        if password1 == '':
            password1_error = "密码不能为空"
            return render(request, 'user/register.html', locals())
        if password1 != password2:
            password2_error = "两次密码不一致!"
            return render(request, 'user/register.html', locals())
        try:
            user = models.User.objects.create(name=username, password=password1)
            return HttpResponseRedirect('/')
        except:
            return HttpResponse('注册失败')


def mylogout(request):
    ''' 注销 '''
    # 判断session中是否有用户信息,有的话删除之后退回主页
    if 'userinfo' in request.session:
        del request.session['userinfo']
    return HttpResponseRedirect("/")
