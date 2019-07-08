from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
from user.models import User
from note.models import Note

user = ""


def check_user(func):
    '''装饰器:用于检查session中是否存在用户信息'''

    def wrapper(request, *args, **kwargs):
        if hasattr(request, 'session') and 'userinfo' in request.session:
            # 此时用户已登陆
            # 拿到用户id
            user_id = request.session['userinfo']['id']
            # 根据当前登陆用户找到当前用户
            global user
            user = User.objects.get(id=user_id)
        else:
            raise Http404
        return func(request, *args, **kwargs)

    return wrapper


@check_user
def showall(request):
    notes = Note.objects.filter(author=user)
    return render(request, 'note/showall.html', locals())


@check_user
def add(request):
    if request.method == 'GET':
        return render(request, "note/create_note.html")
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(title=title, content=content, author=user)
        return HttpResponseRedirect('/note/showall.html')


@check_user
def delete(request, note_id):
    try:
        anote = Note.objects.get(author=user, id=note_id)
        anote.delete()
        return HttpResponseRedirect('/note/showall.html')
    except:
        return HttpResponse("删除失败")


@check_user
def modify(request, note_id):
    if request.method == 'GET':
        anote = Note.objects.get(author=user, id=note_id)
        return render(request, "note/modify_note.html", locals())
    elif request.method == 'POST':
        try:
            anote = Note.objects.get(author=user, id=note_id)
            anote.title = request.POST['title']
            anote.content = request.POST['content']
            anote.save()
            return HttpResponseRedirect("/note/showall.html")
        except:
            return HttpResponse("修改失败")
