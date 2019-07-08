from django.conf.urls import url

from note import views

urlpatterns = [
    # 查看本人的全部笔记
    url(r'^showall',views.showall),
    url(r'^add',views.add),
    url(r'^mod/(\d+)',views.modify),
    url(r'^del/(\d+)',views.delete),
]